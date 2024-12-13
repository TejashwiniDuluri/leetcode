# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root) -> int:
        queue = []
        
        queue.append(root)
        
        depth = 1
        
        while queue:
            curr_depth = []
            le = len(queue)
                
            while le >= 0:
                curr = queue.pop()
                curr_depth.append(curr.val)
                le -= 1
                
                queue.append(curr.left)
                queue.append(curr.right)
            
            depth += 1
        return depth
                
                
                
                            
            
        