# XMSS 多重签名密码学库（后量子以太坊）

本项目是 **IACR 2025/055: Hash-Based Multi-Signatures for Post-Quantum Ethereum** 的概念验证实现（Proof-of-Concept）。  
使用 Python 实现了 **XMSS（扩展 Merkle 签名方案）**，包含 **WOTS+、Merkle 树、签名与验证、聚合功能以及性能测试**。

---

##功能概述
- **Winternitz 一次性签名（WOTS+）**
- **Merkle 树公钥聚合**
- **XMSS 签名与验证**
- **可调节参数的可变哈希函数（SHA3-256 / SHA-256 / Poseidon2 占位）**
- **多重签名聚合（Dummy SNARK 模拟版本）**
- **单元测试与性能测试**
- **一键运行脚本（run_all.py）**

---

## 项目结构
src/
wots.py # WOTS+ 签名算法
merkle.py # Merkle 树构建与路径验证
xmss.py # XMSS 核心签名与验证
hash_fn.py # 可调节哈希函数
encode.py # 不可比较编码（简化版本）
aggregate.py # 签名聚合（Dummy SNARK 模拟）
config.py # 全局参数配置

tests/
test_wots.py # WOTS+ 单元测试
test_merkle.py # Merkle 树单元测试
test_xmss.py # XMSS 单元测试

benchmark/
benchmark_signing.py # 签名性能测试
benchmark_verify.py # 验证性能测试

main.py # 项目演示入口（签名、验证、聚合）
run_all.py # 一键运行所有测试 + 性能测试 + 演示
requirements.txt # Python 依赖
README.md # 项目说明文档


---

##  环境配置
**要求：**
- Python >= 3.8  
- pip 包管理器

安装依赖：
```bash
pip install -r requirements.txt

使用方式
运行演示（签名 + 验证 + 聚合）
python main.py

一键运行（单元测试 + 性能测试 + 演示）
python run_all.py

Benchmark 输出示例:
=== 签名性能测试 ===
平均签名时间: 0.001200 秒
平均签名大小: 4800 字节

=== 验证性能测试 ===
平均验证时间: 0.001800 秒

参数配置:

在 src/config.py 中调整：
HASH_ALGO = "sha3_256"   # 哈希算法
WOTS_PARAM_W = 16        # Winternitz 参数 w
XMSS_LEAVES = 4          # Merkle 树叶子数
XMSS_SEED = "group-project-demo"
BENCHMARK_ITER = 10      # Benchmark 迭代次数

参考资料
Hash-Based Multi-Signatures for Post-Quantum Ethereum, IACR 2025/055

