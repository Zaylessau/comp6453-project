# Incomparable encoding scheme placeholder
# =======================================
# Incomparable Encoding (Simplified)
# =======================================
from src.hash_fn import simple_hash


class IncomparableEncoding:
    @staticmethod
    def encode_message(message: str, domain: str = "XMSS") -> str:
        """
        简化版本：对消息进行域分离编码
        在最终实现中，可根据论文将消息分块并做不可比较编码
        """
        return simple_hash(domain + message)

    @staticmethod
    def decode_message(encoded: str) -> str:
        """
        简化版本：这里无法真正解码，因为编码是不可逆哈希
        在最终系统中，decode 并不是必需
        """
        return encoded  # 占位，不可逆

    @staticmethod
    def chunk_message(message: str, chunk_size: int = 4) -> list:
        """
        将消息分块，方便后续做 WOTS 多块签名
        """
        return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]
