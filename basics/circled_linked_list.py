
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def check_circled(self, node):
        if not node:
            return None

        slow = node.next
        fast = node.next.next

        while fast and fast.next:
            if fast == slow:
                return fast.val

            slow = slow.next
            fast = fast.next.next

        return False

    def get_entry(self, node):
        if not node:
            return None

        encounter_pt = self.check_circled(node)

        if encounter_pt:
            slow = node
            fast = encounter_pt

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


s = Solution()
print (s.check_circled(node1))