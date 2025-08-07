# XMSS Project Configuration

# Hash settings
HASH_ALGO = "sha3_256"      # "sha3_256", "sha256", or Poseidon2
HASH_SIZE = 32              # Hash output size in bytes

# WOTS parameters
WOTS_PARAM_W = 16           # Winternitz parameter w
WOTS_KEY_SIZE = 16          # WOTS key length

# Merkle tree settings
XMSS_LEAVES = 16            # Number of leaf nodes
XMSS_SEED = "group-project-demo"  # Key generation seed

# Benchmark settings
BENCHMARK_ITER = 10         # Number of benchmark iterations

# Aggregation mode
AGGREGATION_MODE = "dummy"  # "dummy" or "real" (zkSNARK in future)
