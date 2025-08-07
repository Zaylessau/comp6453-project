# Merkle Tree implementation placeholder
# =======================================
# Merkle Tree Implementation
# =======================================
import math
from src.hash_fn import simple_hash


class MerkleTree:
    def __init__(self, leaves: list):
        """
        初始化 Merkle 树
        leaves: 公钥列表（WOTS 公钥串）
        """
        self.leaves = leaves
        self.tree = self._build_tree(leaves)

    def _build_tree(self, leaves: list) -> list:
        """
        构造 Merkle 树
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
        获取 Merkle 树根
        """
        return self.tree[-1][0]

    def get_path(self, index: int) -> list:
        """
        获取 index 节点的认证路径
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
        验证 Merkle 路径
        """
        digest = leaf
        for sibling in path:
            if index % 2 == 0:
                digest = simple_hash(digest + sibling)
            else:
                digest = simple_hash(sibling + digest)
            index //= 2
        return digest == root
