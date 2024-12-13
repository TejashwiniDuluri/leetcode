# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root):

        result = []
        if not root:
            return result

        queue = [root]

        while queue:

            queue_len = len(queue)
            level_elem = None

            while queue_len > 0:

                node = queue.pop(0)
                level_elem = node.val
                queue_len -= 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_elem)

        return result
