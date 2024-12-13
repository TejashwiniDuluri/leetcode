# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def __init__(self) -> None:
        self.visit = 0
        self.elem = None
        
    # def kthSmallest(self, root, k) -> int:
    #     return self.inorder(root, k)
        
    def kthSmallest(self, root, k) -> int:        
        
        def inorder(root):
            if root:
                inorder(root.left)
                
                if self.visit == k:
                    self.elem = root.val
                    return
                
                inorder(root.right)
                 
        inorder(root)
        return self.elem
        
                
        