# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p, q) -> bool:
        
        if not p and q  or not q and p:  
            return False
        
        elif not p and not q:
            return True

        elif p.val != q.val:
            return False

        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
                           
        
        
            
            
            
        