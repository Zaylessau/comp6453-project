import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from src.xmss import XMSS
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES, BENCHMARK_ITER


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

    print("\n=== 签名性能测试 ===")
    print(f"测试次数: {BENCHMARK_ITER}")
    print(f"平均签名时间: {avg_time:.6f} 秒")
    print(f"平均签名大小: {avg_size:.2f} 字节")


if __name__ == "__main__":
    benchmark_signing()
