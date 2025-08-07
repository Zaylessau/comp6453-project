import unittest
from src.xmss import XMSS
from src.encode import IncomparableEncoding
from src.aggregate import Aggregator  

class TestAggregator(unittest.TestCase):
    def setUp(self):
        self.encoder = IncomparableEncoding()
        self.message = "aggregate test message"
        self.epoch = 1

        # Create XMSS instances with different seeds
        self.xmss_list = [
            XMSS(seed="seed1", num_leaves=4),
            XMSS(seed="seed2", num_leaves=4),
            XMSS(seed="seed3", num_leaves=4),
        ]

        # Create signatures from index 0 of each XMSS
        self.signatures = []
        for xmss in self.xmss_list:
            encoded_msg = self.encoder.encode_message(self.message)
            sig = xmss.sign(0, encoded_msg)
            pk = xmss.get_public_key()
            self.signatures.append((pk, sig))

    def test_aggregation_and_verification(self):
        aggregator = Aggregator()

        for pk, sig in self.signatures:
            aggregator.add_signature(pk, self.message, sig, self.epoch)

        aggregated_data = aggregator.aggregate()
        self.assertEqual(aggregated_data["num_signatures"], 3)
        self.assertEqual(aggregated_data["message"], self.message)

        # Check dummy proof exists
        self.assertIn("aggregated_proof", aggregated_data)

        # Verify the aggregated signature
        verified = aggregator.verify(aggregated_data)
        self.assertTrue(verified)

    def test_reject_different_message(self):
        aggregator = Aggregator()
        pk, sig = self.signatures[0]
        aggregator.add_signature(pk, self.message, sig, self.epoch)
        with self.assertRaises(AssertionError):
            aggregator.add_signature(pk, "wrong message", sig, self.epoch)

    def test_reject_different_epoch(self):
        aggregator = Aggregator()
        pk, sig = self.signatures[0]
        aggregator.add_signature(pk, self.message, sig, self.epoch)
        with self.assertRaises(AssertionError):
            aggregator.add_signature(pk, self.message, sig, 999)

if __name__ == '__main__':
    unittest.main()
