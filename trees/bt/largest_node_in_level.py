# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root):
        results = []
        if not root:
            return results
        queue = [root]

        while queue:
            queue_len = len(queue)
            sub_level = []

            while queue_len > 0:
                node = queue.pop(0)
                sub_level.append(node.val)
                queue_len -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(max(sub_level))

        return results
