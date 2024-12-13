# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root) -> int:

        ans = 0

        def dfs(root, val):
            nonlocal ans
            if not root:
                return

            val = val * 10
            val += root.val

            if not root.left and not root.right:
                ans += int(val, 2)
                return

            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, 0)
        return ans