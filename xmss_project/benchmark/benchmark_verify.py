# Benchmark for XMSS verification performance

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from src.xmss import XMSS
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES, BENCHMARK_ITER


def benchmark_verification():
    xmss = XMSS(seed=XMSS_SEED, num_leaves=XMSS_LEAVES)
    message = IncomparableEncoding.encode_message("benchmark verify test")

    # Pre-generate signatures for benchmarking
    signatures = [xmss.sign(i, message) for i in range(BENCHMARK_ITER)]
    times = []

    for sig in signatures:
        start = time.time()
        valid = xmss.verify(message, sig)
        end = time.time()
        times.append(end - start)

    avg_time = sum(times) / BENCHMARK_ITER

    print("\n=== Verification Benchmark ===")
    print(f"Iterations: {BENCHMARK_ITER}")
    print(f"Average verification time: {avg_time:.6f} seconds")


if __name__ == "__main__":
    benchmark_verification()
