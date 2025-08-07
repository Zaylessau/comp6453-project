# Entry point for testing XMSS signing and verification
# =======================================
# XMSS Demo Entry Point
# =======================================
from src.xmss import XMSS
from src.aggregate import Aggregator
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES

import time

def demo_xmss_workflow():
    xmss = XMSS(seed=XMSS_SEED, num_leaves=XMSS_LEAVES)

    messages = [
        "Message A",
        "Message B",
        "Message C"
    ]

    encoded_messages = [IncomparableEncoding.encode_message(m) for m in messages]

    signatures = []
    print("\n=== Signing Multiple Messages ===")
    for i, msg in enumerate(encoded_messages):
        start = time.time()
        sig = xmss.sign(i, msg)
        end = time.time()
        print(f"[{i}] Signature index: {sig['index']}, time: {end - start:.6f}s")
        signatures.append(sig)

    print("\n=== Verifying Each Signature ===")
    for i, (msg, sig) in enumerate(zip(encoded_messages, signatures)):
        valid = xmss.verify(msg, sig)
        print(f"[{i}] Signature valid: {valid}")

    print("\n=== Negative Test: Modified Message ===")
    tampered_msg = IncomparableEncoding.encode_message("Tampered Message")
    is_valid = xmss.verify(tampered_msg, signatures[0])
    print("Should be False -> Signature valid:", is_valid)

    print("\n=== Aggregating Signatures ===")
    agg = Aggregator()
    agg.add_signature(signatures[0])
    agg.add_signature(signatures[1])
    agg_sig = agg.aggregate()
    print("Aggregated Proof:", agg_sig["aggregated_proof"])
    print("Total Signatures Aggregated:", agg_sig["num_signatures"])

    print("\n=== Verifying Aggregated Signatures ===")
    valid = agg.verify_aggregate(agg_sig)
    print("Aggregate valid:", valid)


if __name__ == "__main__":
    demo_xmss_workflow()
