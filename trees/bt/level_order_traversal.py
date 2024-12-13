# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root):

        queue = [root]
        results = []

        while queue:
            level_queue = []
            queue_len = len(queue)

            while queue_len > 0:
                node = queue.pop(0)
                queue_len -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level_queue.append(node.val)
            results.append(level_queue)
        return results[::-1]
