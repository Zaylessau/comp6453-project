# Unit tests for XMSS
import unittest
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


if __name__ == "__main__":
    unittest.main()
