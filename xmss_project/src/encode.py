# Incomparable Encoding (Simplified Placeholder)

from src.hash_fn import simple_hash


class IncomparableEncoding:
    @staticmethod
    def encode_message(message: str, domain: str = "XMSS") -> str:
        """
        Encode message with domain separation (one-way hash).
        """
        return simple_hash(domain + message)

    @staticmethod
    def decode_message(encoded: str) -> str:
        """
        Decoding not possible due to one-way hash.
        """
        return encoded  # Placeholder

    @staticmethod
    def chunk_message(message: str, chunk_size: int = 4) -> list:
        """
        Split message into fixed-size chunks.
        """
        return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]
