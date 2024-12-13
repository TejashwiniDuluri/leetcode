# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    

    def maxAncestorDiff(self, root) -> int:        
        final_max = float('-inf')        

        def preorder(node, max_value, min_value):
            nonlocal final_max
            
            max_value = max(max_value, node.val)
            min_value = min(min_value, node.val)
            
            if node.left:
                preorder(node.left, max_value, min_value)
            
            if node.right:
                preorder(node.right, max_value, min_value)

            final_max = max(max_value - min_value, final_max)
            
            return

        preorder(root, root.val, root.val)
        return final_max

tree = TreeNode(8)
tree.left = TreeNode(3)
tree.right = TreeNode(10)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(6)
tree.left.right.left = TreeNode(4)
tree.left.right.right = TreeNode(7)

tree.right.right = TreeNode(14)
tree.right.right.left = TreeNode(13)

obj = Solution()

print(obj.maxAncestorDiff(tree))






        
