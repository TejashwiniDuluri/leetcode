
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root) -> bool:

        status = True

        def traverse(root, height):
            nonlocal status                  
            
            left_height = 0
            right_height = 0

            if not root:
                return height

            if root.left:                
                root.left, left_height = traverse(root.left, left_height)            

            if root.right:
                root.right, right_height = traverse(root.right, right_height)            

            # + root/node

            height = abs(left_height - right_height) + 1
            
            if height > 1:
                status = False

            return root, height
        
        traverse(root, 0)
        return status
    

