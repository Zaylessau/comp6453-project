# Unit tests for MerkleTree

import unittest
from src.merkle import MerkleTree
from src.hash_fn import simple_hash


class TestMerkle(unittest.TestCase):
    def setUp(self):
        # Prepare a Merkle tree with 4 hashed leaf nodes
        self.leaves = [simple_hash(f"leaf{i}") for i in range(4)]
        self.tree = MerkleTree(self.leaves)

    def test_root_not_empty(self):
        # Check that the Merkle root is not empty
        root = self.tree.get_root()
        self.assertTrue(len(root) > 0)

    def test_path_verification(self):
        # Verify that a valid authentication path passes
        index = 0
        path = self.tree.get_path(index)
        self.assertTrue(MerkleTree.verify_path(self.leaves[index], path, index, self.tree.get_root()))

    def test_path_fail(self):
        # Verify that tampered root fails authentication
        index = 0
        path = self.tree.get_path(index)
        tampered_root = "12345"
        self.assertFalse(MerkleTree.verify_path(self.leaves[index], path, index, tampered_root))


if __name__ == "__main__":
    unittest.main()
