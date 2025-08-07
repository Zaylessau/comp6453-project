# Merkle Tree Implementation (Simplified)

import math
from src.hash_fn import simple_hash


class MerkleTree:
    def __init__(self, leaves: list):
        """
        Initialize Merkle tree with a list of leaf nodes (WOTS public keys).
        """
        self.leaves = leaves
        self.tree = self._build_tree(leaves)

    def _build_tree(self, leaves: list) -> list:
        """
        Build the full Merkle tree from leaves upward.
        """
        tree = [leaves]
        current_level = leaves

        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                combined = simple_hash(left + right)
                next_level.append(combined)
            tree.append(next_level)
            current_level = next_level

        return tree

    def get_root(self) -> str:
        """
        Return the Merkle root.
        """
        return self.tree[-1][0]

    def get_path(self, index: int) -> list:
        """
        Return the authentication path for a given leaf index.
        """
        path = []
        for level in self.tree[:-1]:
            sibling_index = index ^ 1
            if sibling_index < len(level):
                path.append(level[sibling_index])
            index //= 2
        return path

    @staticmethod
    def verify_path(leaf: str, path: list, index: int, root: str) -> bool:
        """
        Verify a Merkle authentication path.
        """
        digest = leaf
        for sibling in path:
            if index % 2 == 0:
                digest = simple_hash(digest + sibling)
            else:
                digest = simple_hash(sibling + digest)
            index //= 2
        return digest == root
