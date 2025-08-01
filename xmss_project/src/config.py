# Parameter configuration placeholder
# =============================
# XMSS Project Configuration
# =============================

# Hash settings
HASH_ALGO = "sha3_256"  # 可切换为 "sha256" 或 Poseidon2 实现
HASH_SIZE = 32          # 字节大小（256位）

# WOTS parameters
WOTS_PARAM_W = 16       # Winternitz 参数 w
WOTS_KEY_SIZE = 16      # 私钥/公钥长度

# Merkle tree
XMSS_LEAVES = 16         # 叶节点数量（演示可选 4、8、16）
XMSS_SEED = "group-project-demo"  # 种子

# Benchmark parameters
BENCHMARK_ITER = 10     # Benchmark 签名/验证循环次数

# Aggregation (SNARK simulation)
AGGREGATION_MODE = "dummy"  # 可选: dummy / real (未来支持 zkSNARK)
