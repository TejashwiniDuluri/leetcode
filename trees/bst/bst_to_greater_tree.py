# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def __init__(self) -> None:
    #     self.results = []
    #     self.root = None
    #     self.prev_sum = 0
    #     self.summ = 0
        
    # def convertBST(self, root) :
    #     self.inorder(root)
    #     summ = sum(self.results)
    #     prev_sum = 0
    #     self.replace_values(self, self.root)
    #     return self.root
                
    # def inorder(self, root):
    #     if root:
    #         self.inorder(root.left)
    #         self.results.append(root.val)            
    #         self.inorder(root.right)
            
    # def replace_values(self, root):
        
    #     if root:
    #         self.inorder(root.left)
    #         root.val = self.summ - self.prev_sum
    #         self.prev_sum+= root.val
    #         self.inorder(root.right)
            
            
    ######### optimizing below ########
    
    def __init__(self) -> None:
        self.summ = 0
        
    def convertBST(self, root) :
        self.construct_gt(root)
        
    def construct_gt(self, root):
        if not root:
            return root
        
        self.right = self.construct_gt(root.right)
        tmp = root.val
        root.val += root.val + self.summ
        self.summ = tmp + self.summ
        self.left = self.construct_gt(root.right)
        return root

    