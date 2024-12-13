# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        output = []

        def dfs(root, val):
            nonlocal output
            if not root:
                return

            if not root.left and not root.right:
                val = val + str(root.val)
                output.append(val)
                return

            val = val + str(root.val) + "->"
            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, "")
        return output
