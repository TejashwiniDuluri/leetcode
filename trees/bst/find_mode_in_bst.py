# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findMode(self, root):
        obj = {}
        self.inorder(root, obj)
        result = []
        for key, value in obj.items():
            if value > 1:
                result.append(key)
        return result
    
    def inorder (self, root, obj):
        
        if root:
            if obj.get(root.val):
                obj[root.val] += 1
            if root.left:
                self.inorder(root.left, obj)
            if root.right:
                self.inorder(root.right, obj)
        return root 
        