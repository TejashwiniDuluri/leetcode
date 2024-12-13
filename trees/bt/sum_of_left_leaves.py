# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.sum = 0

    def sumOfLeftLeaves(self, root):
        self.sum_leafs(root)
        return self.sum
        
    def sum_leafs(self, root):
        if not root:
            return None

        if root.left:
            node = self.sum_leafs(root.left)
            if node and not node.left and not node.right:
                self.sum += 1

        if root.right:
            node = self.sum_leafs(root.right)

        return node




        
        
    