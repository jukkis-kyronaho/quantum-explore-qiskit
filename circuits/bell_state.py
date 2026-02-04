from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization
import plot_histogram import matplotlib.pyplot as plt

def bell_state_demo():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    backend = Aer.get_backend("qasm_simulator")
    tqc = transpile(qc, backend)
    result = backend.run(tqc, shots=1024).result()
    counts = result.get_counts()

    print("Bell state counts:", counts)
    plot_histogram(counts)
    plt.show()


if __name__ == "__main__":
    bell_state_demo()
