# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root) -> str:
        ans = "~"

        def dfs(root, val):
            nonlocal ans

            if not root:
                return

            val = chr(root.val + 97) + val

            if not root.left and not root.right:
                ans = min(val, ans)
                return

            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, "")
        return ans
