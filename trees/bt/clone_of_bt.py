# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return None

            if root.val == target.val:
                return root

            left = dfs(root.left)
            right = dfs(root.right)
            return left or right

        return dfs(cloned)
