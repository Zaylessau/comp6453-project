import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from src.xmss import XMSS
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES, BENCHMARK_ITER
import matplotlib.pyplot as plt


def benchmark_verification():
    xmss = XMSS(seed=XMSS_SEED, num_leaves=XMSS_LEAVES)
    message = IncomparableEncoding.encode_message("benchmark verify test")

    signatures = [xmss.sign(i, message) for i in range(BENCHMARK_ITER)]
    times = []

    for sig in signatures:
        start = time.time()
        valid = xmss.verify(message, sig)
        end = time.time()
        times.append(end - start)

    avg_time = sum(times) / BENCHMARK_ITER

    print("\n=== Verification Performance Test ===")
    print(f"Test Iterations: {BENCHMARK_ITER}")
    print(f"Average Verification Time: {avg_time:.6f} seconds")
    plt.figure()
    plt.plot(range(BENCHMARK_ITER), times, marker='o', color='green')
    plt.title("Verification Time per Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.savefig("verification_time.png")
    plt.close()


if __name__ == "__main__":
    benchmark_verification()
