# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isUnivalTree(self, root) -> bool:
        value = root.val
        
        if root:
            if root.val != value:
                return False
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            
            
                
        