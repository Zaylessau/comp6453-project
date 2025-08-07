# XMSS (Extended Merkle Signature Scheme) Implementation

from src.config import XMSS_LEAVES, XMSS_SEED
from src.wots import WOTS
from src.merkle import MerkleTree


class XMSS:
    def __init__(self, seed: str = XMSS_SEED, num_leaves: int = XMSS_LEAVES):
        """
        Initialize XMSS instance with WOTS keys and Merkle tree.
        """
        self.seed = seed
        self.num_leaves = num_leaves

        # Generate WOTS key pairs
        self.wots_keys = [WOTS(seed + str(i)) for i in range(num_leaves)]

        # Collect all WOTS public keys as leaf values
        self.public_keys = [''.join(k.public_key) for k in self.wots_keys]

        # Build Merkle tree and get root
        self.tree = MerkleTree(self.public_keys)
        self.root = self.tree.get_root()

        # Track used leaf indices (one-time usage)
        self.used_indices = set()

    def sign(self, index: int, message: str):
        """
        Sign a message using the WOTS key at the given index.
        Includes the Merkle authentication path.
        """
        if index in self.used_indices:
            raise ValueError(f"Index {index} already used for signing")

        if index >= self.num_leaves:
            raise IndexError("Index exceeds available leaf count")

        self.used_indices.add(index)

        sig_wots = self.wots_keys[index].sign(message)
        auth_path = self.tree.get_path(index)

        return {
            "index": index,
            "signature_wots": sig_wots,
            "auth_path": auth_path,
            "root": self.root
        }

    def verify(self, message: str, signature: dict) -> bool:
        """
        Verify XMSS signature using WOTS verification and Merkle path check.
        """
        index = signature["index"]
        sig_wots = signature["signature_wots"]
        auth_path = signature["auth_path"]
        root = signature["root"]

        wots_instance = self.wots_keys[index]
        if not wots_instance.verify(message, sig_wots):
            return False

        leaf_value = ''.join(wots_instance.public_key)
        return self.tree.verify_path(leaf_value, auth_path, index, root)
