# Tweakable hash functions (SHA-3, Poseidon2 placeholder)
# =======================================
# Tweakable Hash Function Implementation
# =======================================
import hashlib
from src.config import HASH_ALGO, HASH_SIZE


def tweakable_hash(public_param: str, tweak: str, message: str) -> str:
    """
    Tweakable hash: H(P || T || M)
    P: 公共参数 (public_param)
    T: tweak，用于域分离
    M: 消息
    """
    combined = (public_param + tweak + message).encode()

    if HASH_ALGO.lower() == "sha3_256":
        return hashlib.sha3_256(combined).hexdigest()
    elif HASH_ALGO.lower() == "sha256":
        return hashlib.sha256(combined).hexdigest()
    else:
        raise ValueError(f"Unsupported hash algorithm: {HASH_ALGO}")


def simple_hash(data: str) -> str:
    """
    Simple hash function for Merkle tree/WOTS
    """
    if HASH_ALGO.lower() == "sha3_256":
        return hashlib.sha3_256(data.encode()).hexdigest()
    elif HASH_ALGO.lower() == "sha256":
        return hashlib.sha256(data.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported hash algorithm: {HASH_ALGO}")


def get_hash_size() -> int:
    """
    获取哈希输出大小（字节数）
    """
    return HASH_SIZE
