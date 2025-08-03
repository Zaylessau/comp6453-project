# Unit tests for Merkle tree
import unittest
from src.merkle import MerkleTree
from src.hash_fn import simple_hash


class TestMerkle(unittest.TestCase):
    def setUp(self):
        self.leaves = [simple_hash(f"leaf{i}") for i in range(4)]
        self.tree = MerkleTree(self.leaves)

    def test_root_not_empty(self):
        root = self.tree.get_root()
        self.assertTrue(len(root) > 0)

    def test_path_verification(self):
        index = 0
        path = self.tree.get_path(index)
        self.assertTrue(MerkleTree.verify_path(self.leaves[index], path, index, self.tree.get_root()))

    def test_path_fail(self):
        index = 0
        path = self.tree.get_path(index)
        tampered_root = "12345"
        self.assertFalse(MerkleTree.verify_path(self.leaves[index], path, index, tampered_root))

    def test_path_wrong_index(self):
        index = 0
        path = self.tree.get_path(index)
        wrong_index = 1
        self.assertFalse(MerkleTree.verify_path(self.leaves[index], path, wrong_index, self.tree.get_root()))


if __name__ == "__main__":
    unittest.main()
