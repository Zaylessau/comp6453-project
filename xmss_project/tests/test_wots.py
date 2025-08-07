# Unit tests for WOTS

import unittest
from src.wots import WOTS
from src.config import XMSS_SEED


class TestWOTS(unittest.TestCase):
    def setUp(self):
        # Initialize WOTS with fixed seed
        self.wots = WOTS(seed=XMSS_SEED)

    def test_sign_and_verify(self):
        # Valid signature should pass verification
        message = "test message"
        signature = self.wots.sign(message)
        self.assertTrue(self.wots.verify(message, signature))

    def test_invalid_signature(self):
        # Modified signature should fail verification
        message = "test message"
        signature = self.wots.sign(message)
        signature[0] = "tampered"
        self.assertFalse(self.wots.verify(message, signature))


if __name__ == "__main__":
    unittest.main()
