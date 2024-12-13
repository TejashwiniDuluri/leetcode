# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum) -> bool:

        def dfs(root, val):
            if not root:
                return

            val = val + root.val

            #############
            # if not root.left and not root.right:
            #     if val == targetSum:
            #         ans = True
            #     return

            # if not ans:
            #     dfs(root.left, val)
            # if not ans:
            #     dfs(root.right, val)
            ##############

            if not root.left and not root.right:
                if val == targetSum:
                    return True
                return False

            return dfs(root.left, val) or dfs(root.right, val)

        return dfs(root, 0)
