"""showing 1qbit in superposition with a probability amplitude of 1/2^0.5 """


from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


class QuantumBoard:
    def __init__(self, shots: int = 500) -> None:
        """storing core properties"""
        self.shots = shots
        self.simulator = AerSimulator()
        self.circuit = self._build_circuit()

    def _build_circuit(self) -> QuantumCircuit:
        """create circuit and applying Hadamard gate"""
        # qc is a circuit object, and gates are qiskit methods
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        # qbit 0 into bit 0
        qc.measure(0, 0)
        return qc

    def run(self) -> dict[str, int]:
        """500 shots sim"""
        job = self.simulator.run(self.circuit, shots=self.shots)
        res = job.result()
        counts: dict[str, int] = res.get_counts()
        return counts

    def display(self, counts: dict[str, int]) -> None:
        """render circuit diagram, render prob chart, display with matplot"""
        self.circuit.draw("mpl")
        plot_histogram(counts)
        plt.show()


if __name__ == "__main__":
    board = QuantumBoard()
    counts = board.run()
    board.display(counts)
