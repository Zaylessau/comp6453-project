# XMSS Multi-Signature Aggregation (Improved Interface)
# Note: This implementation uses dummy hash-based aggregation for demonstration purposes.

from src.hash_fn import simple_hash
from src.xmss import XMSS

class Aggregator:
    def __init__(self):
        self.pk_sig_pairs = []  # List of (pk, signature) tuples
        self.message = None
        self.epoch = None

    def add_signature(self, pk: str, message: str, signature: dict, epoch: int):
        """
        Add a (pk, signature) pair to the aggregation pool.
        Ensures consistent message and epoch across all signatures.
        """
        if self.message is None:
            self.message = message
        if self.epoch is None:
            self.epoch = epoch

        assert message == self.message, "Inconsistent message across signatures"
        assert epoch == self.epoch, "Inconsistent epoch across signatures"

        self.pk_sig_pairs.append((pk, signature))

    def aggregate(self) -> dict:
        """
        Aggregate all collected signatures by hashing their Merkle roots.
        This simulates the proof of possession (as a placeholder for SNARK proof).
        """
        roots = ''.join(sig["root"] for _, sig in self.pk_sig_pairs)
        proof = simple_hash(roots)

        return {
            "epoch": self.epoch,
            "message": self.message,
            "aggregated_proof": proof,
            "signers": [pk for pk, _ in self.pk_sig_pairs],
            "num_signatures": len(self.pk_sig_pairs),
            "mode": "dummy"
        }

    def verify(self, aggregated_data: dict) -> bool:
        """
        Simulated verification of the aggregated signature.
        Recompute the hash from individual Merkle roots and compare with the proof.
        """
        if aggregated_data["mode"] != "dummy":
            raise NotImplementedError("Only dummy mode is supported")

        if aggregated_data["num_signatures"] != len(self.pk_sig_pairs):
            return False

        # Recompute Merkle root hash
        recomputed_roots = ''.join(sig["root"] for _, sig in self.pk_sig_pairs)
        expected_proof = simple_hash(recomputed_roots)
        return expected_proof == aggregated_data["aggregated_proof"]

    def verify_aggregate(self, result: dict) -> bool:
        return self.verify(result)

