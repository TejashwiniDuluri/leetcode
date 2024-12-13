
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def leafSimilar(self, root1, root2) -> bool:
        return self.traverse(root1, []) == self.traverse(root2, [])

    def traverse(self, root, result):

        if not root:
            return result
        
        if not root.left and not root.right:
            result.append(root.val)
            return result
        
        if root.left:
            self.traverse(root.left, result)
        if root.right:
            self.traverse(root.right, result)
        
        return result
        




        


        