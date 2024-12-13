"""
# Definition for a Node.

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if not root:
            return root
        queue = [root]

        while queue:

            queue_len = len(queue)
            level = None

            while queue_len > 0:
                node = queue.pop(0)
                queue_len -= 1

                node.next = level
                level = node

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return root
