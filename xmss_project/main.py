# Entry point for XMSS signing, verification, and aggregation demo

from src.xmss import XMSS
from src.aggregate import Aggregator
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES


def demo_xmss_workflow():
    # Initialize two XMSS signers
    xmss1 = XMSS(seed=XMSS_SEED + "A", num_leaves=XMSS_LEAVES)
    xmss2 = XMSS(seed=XMSS_SEED + "B", num_leaves=XMSS_LEAVES)

    # Shared message and epoch for aggregation
    message = "hello aggregation"
    encoded_msg = IncomparableEncoding.encode_message(message)
    epoch = 1

    # Sign message with both XMSS instances
    print("\n--- Signing Message ---")
    signature1 = xmss1.sign(0, encoded_msg)
    signature2 = xmss2.sign(0, encoded_msg)

    print("Signature 1 index:", signature1["index"])
    print("Signature 2 index:", signature2["index"])
    print("Merkle Root 1:", signature1["root"])
    print("Merkle Root 2:", signature2["root"])

    # Verify signatures
    print("\n--- Verifying Signatures ---")
    valid1 = xmss1.verify(encoded_msg, signature1)
    valid2 = xmss2.verify(encoded_msg, signature2)
    print("Signature 1 valid:", valid1)
    print("Signature 2 valid:", valid2)

    # Public keys for aggregation
    pk1 = xmss1.get_public_key()
    pk2 = xmss2.get_public_key()

    # Aggregate signatures
    print("\n--- Aggregating Signatures ---")
    aggregator = Aggregator()
    aggregator.add_signature(pk1, message, signature1, epoch)
    aggregator.add_signature(pk2, message, signature2, epoch)

    aggregated_result = aggregator.aggregate()
    print("Aggregated Proof:", aggregated_result["aggregated_proof"])
    print("Total Signatures Aggregated:", aggregated_result["num_signatures"])

    # Verify aggregated result
    print("\n--- Verifying Aggregated Signatures ---")
    agg_valid = aggregator.verify_aggregate(aggregated_result)
    print("Aggregate valid:", agg_valid)


if __name__ == "__main__":
    demo_xmss_workflow()
