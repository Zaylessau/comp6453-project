# Signature Aggregation Logic (SNARK Simulation Placeholder)
# XMSS Multi-Signature Aggregation 

from src.hash_fn import simple_hash
from src.config import AGGREGATION_MODE


class Aggregator:
    def __init__(self):
        self.signatures = []

    def add_signature(self, xmss_signature: dict):
        """
        Add a single XMSS signature to the aggregation pool.
        """
        self.signatures.append(xmss_signature)

    def aggregate(self) -> dict:
        """
        Aggregate all collected signatures (dummy version).
        Simulates zkSNARK aggregation by hashing all Merkle roots.
        """
        if AGGREGATION_MODE == "dummy":
            combined_data = ''.join(sig["root"] for sig in self.signatures)
            proof = simple_hash(combined_data)
            return {
                "aggregated_proof": proof,
                "num_signatures": len(self.signatures),
                "mode": AGGREGATION_MODE
            }
        else:
            raise NotImplementedError("Real zkSNARK aggregation not implemented")

    def verify_aggregate(self, aggregated_data: dict) -> bool:
        """
        Verify the aggregated proof (dummy version).
        """
        if AGGREGATION_MODE == "dummy":
            return aggregated_data["num_signatures"] == len(self.signatures)
        else:
            raise NotImplementedError("Real zkSNARK verification not implemented")
