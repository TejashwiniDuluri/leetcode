
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root, low, high) :
        
    #     return self.summation(root, low, high, 0)
    
    # def summation(self, root, low, high, total_sum):        
        
    #     if root:
    #         if low < root.val < high:
    #             total_sum +=  root.val
            
    #         total_sum += self.summation(root.left, low, high, total_sum)       
    #         total_sum += self.summation(root.right, low, high, total_sum)
    #     return total_sum     
    
    
        if not root:
            return 0
        
        total_sum = 0
        if low <= root.val <= high:
            total_sum += root.val
        if root.val < high:
            total_sum += self.rangeSumBST(root.right, low, high)
        if root.val > low:
            total_sum += self.rangeSumBST(root.left, low, high)
        return total_sum       
            
        
        
        