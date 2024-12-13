# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.hashmap = {}
        self.result = False
        
    def findTarget(self, root, k) :
                
        if root:
            val = root.val            
            if self.hashmap(k - val):
                self.result = True
                return self.result
            self.findTarget(root.left, k)
            self.findTarget(root.right, k)
            
        return self.result
        