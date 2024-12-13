# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.results = []
        
    def balanceBST(self, root):
        self.inorder(root)
        
        return self.construct_bst()
            
    def construct_bst(self, nums):
        le = len(nums)
        if le == 0:
            return None
        
        mid = le//2
        left = nums[:mid]
        right = nums[mid+1:]
        
        tree = TreeNode(nums[mid])
        tree.left = self.construct_bst(left)
        tree.right = self.construct_bst(right)
        return tree
        
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.results.append(root.val)
            self.inorder(root.right)
        return root
                
                
            
        
        