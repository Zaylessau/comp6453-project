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
src/wots.py             
src/merkle.py           
src/xmss.py             
src/hash_fn.py          
src/encode.py             
src/aggregate.py        
src/config.py           

tests/test_wots.py      
tests/test_merkle.py     
tests/test_xmss.py      

benchmark/benchmark_signing.py   # Benchmark signing performance  
benchmark/benchmark_verify.py    # Benchmark verification performance  

main.py                  
run_all.py              
requirements.txt        
README.md               


## Environment Setup

**Requirements:**
- Python >= 3.8
- `pip` package manager

### Install dependencies:

pip install -r requirements.txt

### Usage
Run demo (signing + verification + aggregation):
python main.py

Run all (unit tests + performance benchmarks + demo):
python run_all.py

### Example Benchmark Output:
Signing Benchmark:
Average signing time: 0.001200 sec  
Average signature size: 4800 bytes  

Verification Benchmark:
Average verification time: 0.001800 sec

Parameter Configuration
You can adjust cryptographic parameters in src/config.py:
HASH_ALGO = "sha3_256"       
WOTS_PARAM_W = 16            
XMSS_LEAVES = 4              
XMSS_SEED = "group-project-demo"  
BENCHMARK_ITER = 100          

### Reference
Hash-Based Multi-Signatures for Post-Quantum Ethereum, IACR 2025/055
https://eprint.iacr.org/2025/055
