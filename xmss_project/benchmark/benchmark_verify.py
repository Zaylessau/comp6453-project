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

    signatures = [xmss.sign(i, message) for i in range(BENCHMARK_ITER)]
    times = []

    for sig in signatures:
        start = time.time()
        valid = xmss.verify(message, sig)
        end = time.time()
        times.append(end - start)

    avg_time = sum(times) / BENCHMARK_ITER

    print("\n=== 验证性能测试 ===")
    print(f"测试次数: {BENCHMARK_ITER}")
    print(f"平均验证时间: {avg_time:.6f} 秒")


if __name__ == "__main__":
    benchmark_verification()
