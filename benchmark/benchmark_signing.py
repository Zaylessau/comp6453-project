import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from src.xmss import XMSS
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES, BENCHMARK_ITER
import matplotlib.pyplot as plt


def benchmark_signing():
    xmss = XMSS(seed=XMSS_SEED, num_leaves=XMSS_LEAVES)
    message = IncomparableEncoding.encode_message("benchmark signing test")

    times = []
    sizes = []

    for i in range(BENCHMARK_ITER):
        start = time.time()
        sig = xmss.sign(i, message)
        end = time.time()

        times.append(end - start)
        sizes.append(len(str(sig)))

    avg_time = sum(times) / BENCHMARK_ITER
    avg_size = sum(sizes) / BENCHMARK_ITER

    print("\n=== Signature Performance Test ===")
    print(f"Test Iterations: {BENCHMARK_ITER}")
    print(f"Average Signing Time: {avg_time:.6f} seconds")
    print(f"Average Signature Size: {avg_size:.2f} bytes")
    plt.figure()
    plt.plot(range(BENCHMARK_ITER), times, marker='o')
    plt.title("Signature Time per Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.savefig("signature_time.png")  # 保存为图片
    plt.close()


if __name__ == "__main__":
    benchmark_signing()
