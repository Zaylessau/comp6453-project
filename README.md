# XMSS Multi-Signature Cryptographic Library (Post-Quantum Ethereum)

This project is a **Proof-of-Concept (PoC) implementation of IACR 2025/055: Hash-Based Multi-Signatures for Post-Quantum Ethereum**.  
It is implemented in Python and features **XMSS (eXtended Merkle Signature Scheme)** with support for **WOTS+, Merkle tree, signing and verification, aggregation functionality, and performance benchmarking**.

---

## Features Overview

- **Winternitz One-Time Signature (WOTS+)**
- **Merkle Tree Public Key Aggregation**
- **XMSS Signing and Verification**
- **Configurable Hash Functions** (SHA3-256 / SHA-256 / Poseidon2 placeholder)
- **Multi-Signature Aggregation** (Dummy SNARK Simulation)
- **Unit Tests and Benchmarking**
- **One-Click Execution Script** (`run_all.py`)

---

## Project Structure
<pre><code>``` project-root/ ├── src/ │ ├── wots.py # WOTS+ signature algorithm │ ├── merkle.py # Merkle tree construction and authentication │ ├── xmss.py # XMSS core signing and verification │ ├── hash_fn.py # Configurable hash functions (SHA3-256, etc.) │ ├── encode.py # Non-comparable encoding (simplified) │ ├── aggregate.py # Dummy SNARK-style signature aggregation │ └── config.py # Global parameter configuration │ ├── tests/ │ ├── test_wots.py # Unit tests for WOTS+ │ ├── test_merkle.py # Unit tests for Merkle tree │ └── test_xmss.py # Unit tests for XMSS │ ├── benchmark/ │ ├── benchmark_signing.py # Benchmark signing speed & size │ └── benchmark_verify.py # Benchmark verification speed │ ├── main.py # Demo entry (sign + verify + aggregate) ├── run_all.py # One-click run: tests + benchmarks + demo ├── requirements.txt # Python dependencies └── README.md # Project documentation ``` </code></pre>

## Environment Setup

**Requirements:**
- Python >= 3.8
- `pip` package manager

### Install dependencies:

```bash
pip install -r requirements.txt

Usage
Run demo (signing + verification + aggregation):
python main.py

Run all (unit tests + performance benchmarks + demo):
python run_all.py

Example Benchmark Output:
=== Signing Benchmark ===
Average signing time: 0.001200 sec  
Average signature size: 4800 bytes  

=== Verification Benchmark ===
Average verification time: 0.001800 sec

Parameter Configuration
You can adjust cryptographic parameters in src/config.py:
HASH_ALGO = "sha3_256"       # Hash algorithm: sha3_256, sha256, etc.
WOTS_PARAM_W = 16            # Winternitz parameter w
XMSS_LEAVES = 4              # Number of leaves in Merkle tree
XMSS_SEED = "group-project-demo"  # Seed for key generation
BENCHMARK_ITER = 10          # Number of iterations for benchmarking

Reference
Hash-Based Multi-Signatures for Post-Quantum Ethereum, IACR 2025/055
https://eprint.iacr.org/2025/055