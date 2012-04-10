from collections import deque

class TreeNode:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.children = []

def link(parent, child):
	parent.children.append(child)
	child.parent = parent


class BinaryTree:
	def __init__(self, root):
		
		if not root:
			raise ValueError("Root node can not be null") 

		self.root = root

def DepthFirstSearch(root, value):
	stack = deque()
	stack.appendleft(root)
	while len(stack) != 0:
		current = stack.pop()
		if current.value == value:
			return current

		for child in current.children:
			stack.appendleft(child)

	return None
