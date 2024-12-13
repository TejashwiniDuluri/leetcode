# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        results = []

        def dfs(root, routes, route_sum):
            nonlocal results
            if not root:
                return

            routes.append(root.val)
            route_sum = route_sum + root.val

            if not root.left and not root.right:
                if route_sum == targetSum:
                    results.append(routes)
                return

            dfs(root.left, routes, route_sum)
            dfs(root.right, routes, route_sum)

        dfs(root, [], 0)
        return results


