

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def construct_binary_tree(self, preorder, middleorder):
        if not preorder or not middleorder:
            return None

        root = TreeNode(preorder[0])
        lr_separator = middleorder.index(preorder[0])

        left_in_top = preorder[1: lr_separator + 1]
        left_in_middle = middleorder[0: lr_separator]

        right_in_top = preorder[lr_separator + 1:]
        right_in_middle = middleorder[lr_separator + 1:]

        root.right = self.construct_binary_tree(right_in_top, right_in_middle)
        root.left = self.construct_binary_tree(left_in_top, left_in_middle)

        return root

    def recursion_preorder_traversal(self, root):
        if not root:
            return

        print (root.val)

        self.recursion_preorder_traversal(root.left)
        self.recursion_preorder_traversal(root.right)

    def iteration_preorder_traversal(self, root):
        if not root:
            return

        tree_node_stack = []
        node = root

        while node or tree_node_stack:
            while node:
                print (node.val)
                # Save the node for later finding right nodes
                tree_node_stack.append(node)
                node = node.left

            # Now left nodes are done, back for right nodes
            if tree_node_stack:
                node = tree_node_stack.pop()
                node = node.right

    def recursion_middleorder_traversal(self, root):
        if not root:
            return

        self.recursion_middleorder_traversal(root.left)

        print (root.val)

        self.recursion_middleorder_traversal(root.right)

    def iteration_middleorder_traversal(self, root):
        if not root:
            return

        tree_node_stack = []
        node = root

        while node or tree_node_stack:
            while node:
                tree_node_stack.append(node)
                node = node.left

            if tree_node_stack:
                node = tree_node_stack.pop()
                print (node.val)
                node = node.right

    def recursion_postorder_traversal(self, root):
        if not root:
            return

        self.recursion_postorder_traversal(root.left)
        self.recursion_postorder_traversal(root.right)

        print (root.val)

    def iteration_postorder_traversal(self, root):
        if not root:
            return

        tree_node_stack1 = []
        tree_node_stack2 = []
        node = root
        tree_node_stack1.append(node)

        while tree_node_stack1:
            node = tree_node_stack1.pop()
            if node.left:
                tree_node_stack1.append(node.left)
            if node.right:
                tree_node_stack1.append(node.right)
            tree_node_stack2.append(node)
        while tree_node_stack2:
            node_out = tree_node_stack2.pop()
            print (node_out.val)

    def level_queue(self, root):
        if root == None:
            return

        tree_node_queue = []
        node = root
        tree_node_queue.append(node)

        while tree_node_queue:
            node = tree_node_queue.pop(0)
            print (node.val)

            if node.left:
                tree_node_queue.append(node.left)

            if node.right:
                tree_node_queue.append(node.right)


if __name__ == '__main__':
    top = [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
    middle = [7, 3, 8, 1, 4, 9, 0, 5, 2, 6]
    s = Solution()
    tree = s.construct_binary_tree(top, middle)
    print ("preorder: "), s.recursion_preorder_traversal(tree)
    print ("preorder: "), s.iteration_preorder_traversal(tree)
    print ("middleorder: "), s.recursion_middleorder_traversal(tree)
    print ("middleorder: "), s.iteration_middleorder_traversal(tree)
    print ("postorder: "), s.recursion_postorder_traversal(tree)
    print ("postorder: "), s.iteration_postorder_traversal(tree)