from collections import deque

class TreeNode:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.children = []

	def __repr__(self):
		return str(self.value)

def link(parent, child):
	parent.children.append(child)
	child.parent = parent


class BinaryTree:
	def __init__(self, root):
		
		if not root:
			raise ValueError("Root node can not be null") 

		self.root = root


class TreeAdapter:
	def __init__(self):
		self.deque = deque()

	def add(self, value):
		self.deque.appendleft(value)

	def __len__(self):
		return len(self.deque)

class StackAdapter(TreeAdapter):
	def remove(self):
		return self.deque.popleft()

class QueueAdapter(TreeAdapter):
	def remove(self):
		return self.deque.pop()

class TreeIterator:
	def __init__(self, structure_adapter, root):
		self.structure_adapter = structure_adapter
		self.root = root

	def __iter__(self):
		to_process = self.structure_adapter
		to_process.add(self.root)
		while len(to_process) != 0:
			current = to_process.remove()
			yield current
			for child in current.children:
				to_process.add(child)

class DepthFirstIterator(TreeIterator):
	def __init__(self, root):
		TreeIterator.__init__(self, StackAdapter(), root)

class BreadthFirstIterator(TreeIterator):
	def __init__(self, root):
		TreeIterator.__init__(self, QueueAdapter(), root)

def TreeSearch(root, value, iterator):
	for node in iterator(root):
		if value == node.value:
			return node

def BreadthFirstSearch(root, value):
	return TreeSearch(root, value, BreadthFirstIterator)

def DepthFirstSearch(root, value):
	return TreeSearch(root, value, DepthFirstIterator)