

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def construct_binary_tree(self, top, middle):
		if not top or not middle:
			return None

		root = TreeNode(top[0])
		lr_separator= middle.index(top[0])

		left_in_top = top[1 : lr_separator + 1]
		left_in_middle = middle[0 : lr_separator]

		right_in_top = top[lr_separator + 1 : ]
		right_in_middle = middle[lr_separator + 1 : ]

		root.right = self.construct_binary_tree(right_in_top, right_in_middle)
		root.left = self.construct_binary_tree(left_in_top, left_in_middle)

		return root
