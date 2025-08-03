# Unit tests for XMSS
import unittest
import random
import string
from src.xmss import XMSS
from src.encode import IncomparableEncoding
from src.config import XMSS_SEED, XMSS_LEAVES


class TestXMSS(unittest.TestCase):
    def setUp(self):
        self.xmss = XMSS(seed=XMSS_SEED, num_leaves=XMSS_LEAVES)

    def test_sign_and_verify(self):
        message = IncomparableEncoding.encode_message("hello test")
        signature = self.xmss.sign(0, message)
        self.assertTrue(self.xmss.verify(message, signature))

    def test_double_use_index(self):
        message = IncomparableEncoding.encode_message("first use")
        self.xmss.sign(0, message)
        with self.assertRaises(ValueError):
            self.xmss.sign(0, message)  # 再次使用同 index 应报错

    def test_invalid_signature(self):
        message = IncomparableEncoding.encode_message("hello test")
        signature = self.xmss.sign(1, message)
        signature["root"] = "tampered"
        self.assertFalse(self.xmss.verify(message, signature))

    def test_sign_invalid_index(self):
        message = IncomparableEncoding.encode_message("out of range")
        with self.assertRaises(IndexError):
            self.xmss.sign(XMSS_LEAVES, message)

    def test_verify_wrong_message(self):
        message = IncomparableEncoding.encode_message("correct")
        signature = self.xmss.sign(2, message)
        wrong_message = IncomparableEncoding.encode_message("incorrect")
        self.assertFalse(self.xmss.verify(wrong_message, signature))

    def test_sign_and_verify_random_messages(self):
        random.seed(0)
        alphabet = string.ascii_letters + string.digits
        for idx in range(3):
            msg_str = "".join(random.choices(alphabet, k=20))
            message = IncomparableEncoding.encode_message(msg_str)
            signature = self.xmss.sign(idx, message)
            self.assertTrue(self.xmss.verify(message, signature))


if __name__ == "__main__":
    unittest.main()
