# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # def increasingBST(self, root) :
    #     array = []
    #     self.inorder(root, array)
    #     root = array[0]
    #     curr = root
    #     for i in array[1:]:
    #         curr.right = i
    #         curr = i
    #     return root
    
    # def inorder(self, root, array)  :      
        
    #     if root:
    #         if root.left:
    #             self.increasingBST(root.left)
    #         array.append(root)
    #         if root.right:
    #             self.increasingBST(root.right)
    #     return root
        
    def increasingBST(self, root):
        
        self.curr = TreeNode(0)
        self.inorder(root)
        return self.curr.right


    def inorder(self, root):  

        if root:
            self.inorder(root.left)
            curr = root
            curr.left = None
            self.curr.right = curr
            self.curr = curr            
            self.inorder(root.right)





        
        