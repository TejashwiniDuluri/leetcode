# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def __init__(self) -> None:
        self.root = None
        self.preorder_results = []
        
    def bstFromPreorder(self, preorder) :
        for i in preorder:
            self.insert(self.root, i)
        return self.root
        
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        elif val < root.val:
            root.left = self.insert(root.left, val)
        
        elif val > root.val:
            root.right = self.insert(root.right, val)
        
        return root
        
      
    
           