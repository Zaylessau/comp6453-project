# Tweakable Hash Functions (SHA-3, Poseidon2 Placeholder)

import hashlib
from src.config import HASH_ALGO, HASH_SIZE


def tweakable_hash(public_param: str, tweak: str, message: str) -> str:
    """
    Compute tweakable hash: H(P || T || M)
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
    Compute simple hash for Merkle tree or WOTS usage.
    """
    if HASH_ALGO.lower() == "sha3_256":
        return hashlib.sha3_256(data.encode()).hexdigest()
    elif HASH_ALGO.lower() == "sha256":
        return hashlib.sha256(data.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported hash algorithm: {HASH_ALGO}")


def get_hash_size() -> int:
    """
    Return hash output size in bytes.
    """
    return HASH_SIZE
