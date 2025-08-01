# Signature aggregation logic (SNARK simulation placeholder)
# =======================================
# XMSS Multi-Signature Aggregation (Dummy)
# =======================================
from src.hash_fn import simple_hash
from src.config import AGGREGATION_MODE


class Aggregator:
    def __init__(self):
        self.signatures = []

    def add_signature(self, xmss_signature: dict):
        """
        添加 XMSS 签名到聚合池
        """
        self.signatures.append(xmss_signature)

    def aggregate(self) -> dict:
        """
        聚合签名（Dummy 版本）
        实际 SNARK 聚合会将多个签名压缩为简短证明，这里我们用 hash 模拟
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
        验证聚合签名（Dummy 版本）
        """
        if AGGREGATION_MODE == "dummy":
            return aggregated_data["num_signatures"] == len(self.signatures)
        else:
            raise NotImplementedError("Real zkSNARK verification not implemented")
