# Entry point for XMSS signing, verification, and aggregation demo

from src.xmss import XMSS
from src.aggregate import Aggregator
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES


def demo_xmss_workflow():
    # Initialize XMSS
    xmss = XMSS(seed=XMSS_SEED, num_leaves=XMSS_LEAVES)

    # Example message 1
    message = "hello blockchain"
    encoded_msg = IncomparableEncoding.encode_message(message)

    # Sign message
    print("\n--- Signing Message ---")
    signature1 = xmss.sign(0, encoded_msg)
    print("Signature index:", signature1["index"])
    print("Merkle Root:", signature1["root"])

    # Verify signature
    print("\n--- Verifying Signature ---")
    valid = xmss.verify(encoded_msg, signature1)
    print("Signature valid:", valid)

    # Sign a second message
    message2 = "ethereum pq"
    encoded_msg2 = IncomparableEncoding.encode_message(message2)
    signature2 = xmss.sign(1, encoded_msg2)

    # Aggregate both signatures
    print("\n--- Aggregating Signatures ---")
    aggregator = Aggregator()
    aggregator.add_signature(signature1)
    aggregator.add_signature(signature2)

    aggregated_result = aggregator.aggregate()
    print("Aggregated Proof:", aggregated_result["aggregated_proof"])
    print("Total Signatures Aggregated:", aggregated_result["num_signatures"])

    # Verify aggregated result
    print("\n--- Verifying Aggregated Signatures ---")
    agg_valid = aggregator.verify_aggregate(aggregated_result)
    print("Aggregate valid:", agg_valid)


if __name__ == "__main__":
    demo_xmss_workflow()
