# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root) -> bool:

        if root:
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)
            if left and right:
                if root.val == 2:
                    root.val = left.val or right.val
                else:
                    root.val = left.val and right.val
        return root.val
