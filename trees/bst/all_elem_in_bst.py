# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def getAllElements(self, root1, root2):
        results = []
        self.inorder(root1)
        self.inorder(root2)        
        results.sort()
        return results
    
    def inorder(self, root, results):
        
        if root:
            if root.left:
                self.inorder(root.left)                
            results.append(root.val)
            if root.right:
                self.inorder(root.right)
    
            