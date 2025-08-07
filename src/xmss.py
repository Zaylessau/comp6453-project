# XMSS implementation placeholder
# =======================================
# XMSS (Extended Merkle Signature Scheme)
# =======================================
from src.config import XMSS_LEAVES, XMSS_SEED
from src.wots import WOTS
from src.merkle import MerkleTree


class XMSS:
    def __init__(self, seed: str = XMSS_SEED, num_leaves: int = XMSS_LEAVES):
        """
        初始化 XMSS 签名系统
        seed: 随机种子
        num_leaves: Merkle 树叶节点数量
        """
        self.seed = seed
        self.num_leaves = num_leaves

        # 生成多个 WOTS 实例
        self.wots_keys = [WOTS(seed + str(i)) for i in range(num_leaves)]

        # 收集所有 WOTS 公钥（拼接成字符串）
        self.public_keys = [''.join(k.public_key) for k in self.wots_keys]

        # 构造 Merkle 树
        self.tree = MerkleTree(self.public_keys)
        self.root = self.tree.get_root()

        # 记录已使用的 index，避免重复使用
        self.used_indices = set()

    def sign(self, index: int, message: str):
        """
        使用指定 index 的 WOTS 签名，并附带 Merkle 路径
        """
        if index in self.used_indices:
            raise ValueError(f"Index {index} already used for signing (XMSS 一次性签名限制)")

        if index >= self.num_leaves:
            raise IndexError("Index exceeds available leaf count")

        # 标记 index 已使用
        self.used_indices.add(index)

        # 签名
        sig_wots = self.wots_keys[index].sign(message)

        # Merkle 路径
        auth_path = self.tree.get_path(index)

        return {
            "index": index,
            "signature_wots": sig_wots,
            "auth_path": auth_path,
            "root": self.root
        }

    def verify(self, message: str, signature: dict) -> bool:
        """
        验证 XMSS 签名
        """
        index = signature["index"]
        sig_wots = signature["signature_wots"]
        auth_path = signature["auth_path"]
        root = signature["root"]

        # 先验证 WOTS 公钥是否匹配
        wots_instance = self.wots_keys[index]
        if not wots_instance.verify(message, sig_wots):
            return False

        # 重构 WOTS 公钥串
        leaf_value = ''.join(wots_instance.public_key)

        # 验证 Merkle 路径
        return self.tree.verify_path(leaf_value, auth_path, index, root)
