import tree
import unittest

class TreeNodeTest(unittest.TestCase):
	def test_init(self):
		node = tree.TreeNode(5)
		self.assertEqual(5, node.value)
		self.assertEqual(None, node.parent)
		self.assertEqual([], node.children)


class BinaryTreeTest(unittest.TestCase):
	def test_init(self):
		with self.assertRaises(ValueError):
			tree.BinaryTree(None)

		node = tree.TreeNode(5)
		Btree = tree.BinaryTree(node)
		self.assertEqual(node, Btree.root)

	def test_link(self):
		node1 = tree.TreeNode(2)
		node2 = tree.TreeNode(3)
		node3 = tree.TreeNode(5)

		tree.link(node1, node2)
		tree.link(node1, node3)

		self.assertEqual(None, node1.parent)
		self.assertEqual(node2, node1.children[0])
		self.assertEqual(node1, node2.parent)
		self.assertEqual([], node2.children)

		self.assertEqual(node3, node1.children[1])
		self.assertEqual(node1, node3.parent)
		self.assertEqual([], node3.children)

class DepthFirstSearchTest(unittest.TestCase):
	def test_triangle(self):
		node1 = tree.TreeNode(1)
		node2 = tree.TreeNode(4)
		node3 = tree.TreeNode(6)

		tree.link(node1, node2)
		tree.link(node1, node3)

		self.assertEqual(node1, tree.DepthFirstSearch(node1, 1))
		self.assertEqual(node2, tree.DepthFirstSearch(node1, 4))
		self.assertEqual(node3, tree.DepthFirstSearch(node1, 6))
		self.assertEqual(None, tree.DepthFirstSearch(node1, 7))
		


if __name__ == '__main__':
	unittest.main()

