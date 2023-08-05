import os

import pytest
import qiskit

import bluequbit


@pytest.mark.skipif(
    "BLUEQUBIT_STRESS_TESTS" not in os.environ, reason="Requires env variable to be set"
)
def test_gpu_job():
    dq_client = bluequbit.BQClient()
    # time_now = "2022-10-19T13:05:17.917290Z"
    n = 10  # will get to GPU1
    qc_qiskit = qiskit.QuantumCircuit(n)
    for i in range(n):
        qc_qiskit.h(i)
    qc_qiskit.measure_all()

    job_result = dq_client.run(qc_qiskit, job_name="testing_gpu_qiskit", device="gpu")
    print(job_result)

    assert job_result.run_status == "COMPLETED"


@pytest.mark.skipif(
    "BLUEQUBIT_STRESS_TESTS" not in os.environ, reason="Requires env variable to be set"
)
def test_gpu_job_cirq():
    import cirq

    dq_client = bluequbit.BQClient()
    n = 33
    qc = cirq.Circuit()
    qs = cirq.LineQubit.range(n)
    for i in range(n):
        qc.append(cirq.H(qs[i]))
    qc.append(cirq.measure(qs))
    job_result = dq_client.run(qc, job_name="testing_gpu_cirq", device="gpu")
    assert job_result.run_status == "COMPLETED"
