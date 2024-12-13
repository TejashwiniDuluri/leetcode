
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root) -> int:
        left_depth = self.left_depth(root.left)
        right_depth = self.left_depth(root.right)

        if left_depth == right_depth:
            return (2**left_depth) -1
        else:
            #root + left sub tree + ritgh sub tree
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    
    def left_depth(self,root):
        dep = 0

        while root:
            root = root.left
            dep+=1
        return dep

    def right_depth(self,root):
        dep = 0

        while root:
            root = root.right
            dep+=1
        return dep