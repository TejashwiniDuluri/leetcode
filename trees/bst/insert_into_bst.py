# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
   
    def insertIntoBST(self, root, val) :
        
        curr = root
        
        if not curr:
            return TreeNode(val)
            
        while True:        
                        
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left
            elif val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
            
                
     
    # def insertIntoBST(self, root, val) :
    #     root = self._insertIntoBST(root, val)
    #     return root
    
    # def _insertIntoBST(self, root, val) :
    #     if not root:
    #         return TreeNode(val)
        
    #     if val < root.val:
    #         root.left = self._insertIntoBST(root.left, val)
    #     elif val > root.val:
    #         root.right = self._insertIntoBST(root.right, val)
        
    #     return root
            
        
tree = Solution()
tree.
print(tree.insertIntoBST(root))
        