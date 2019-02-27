import unittest

class Node:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def print_list_from_tail_to_head(self, Node):
		if not Node:
			return []

		output_list = []
		current_node = Node

		while current_node:
			output_list.insert(0, current_node.val)
			current_node = current_node.next

		return output_list

class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.s = Solution()

	def test_linked_list(self):
		node1 = Node(10)
		node2 = Node(20)
		node3 = Node(30)

		node1.next = node2
		node2.next = node3

		self.assertEqual(self.s.print_list_from_tail_to_head(node1), [30, 20, 10])

	def test_one_node(self):
		node1 = Node(10)
		self.assertEqual(self.s.print_list_from_tail_to_head(node1), [10])

	def test_empty_node(self):
		node1 = Node(10)
		node2 = Node(None)
		node3 = Node(30)

		node1.next = node2
		node2.next = node3

		self.assertEqual(self.s.print_list_from_tail_to_head(node1), [30, None, 10])






if __name__ == '__main__':
	unittest.main()