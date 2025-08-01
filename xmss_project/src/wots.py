# Winternitz One-Time Signature implementation placeholder
# =======================================
# Winternitz One-Time Signature (WOTS+)
# =======================================
import random
from src.config import WOTS_PARAM_W, WOTS_KEY_SIZE, XMSS_SEED
from src.hash_fn import simple_hash


class WOTS:
    def __init__(self, seed: str = XMSS_SEED):
        random.seed(seed)
        # 私钥是随机生成的一组字符串
        self.private_key = [self._random_hex(32) for _ in range(WOTS_KEY_SIZE)]
        # 公钥是对私钥进行多次 hash
        self.public_key = [self._hash_chain(sk, WOTS_PARAM_W - 1) for sk in self.private_key]

    def _random_hex(self, n: int) -> str:
        return ''.join(random.choices('0123456789abcdef', k=n))

    def _hash_chain(self, value: str, steps: int) -> str:
        """
        对 value 进行多次 hash，形成链
        """
        for _ in range(steps):
            value = simple_hash(value)
        return value

    def sign(self, message: str) -> list:
        """
        WOTS 签名：将消息的每个字符映射到不同的 hash 链位置
        """
        digest = simple_hash(message)
        signature = []
        for i in range(WOTS_KEY_SIZE):
            steps = int(digest[i % len(digest)], 16) % WOTS_PARAM_W
            signature.append(self._hash_chain(self.private_key[i], steps))
        return signature

    def verify(self, message: str, signature: list) -> bool:
        """
        验证：签名通过剩余 hash 迭代恢复到公钥
        """
        digest = simple_hash(message)
        for i in range(WOTS_KEY_SIZE):
            steps = WOTS_PARAM_W - (int(digest[i % len(digest)], 16) % WOTS_PARAM_W) - 1
            computed_pk = self._hash_chain(signature[i], steps)
            if computed_pk != self.public_key[i]:
                return False
        return True
