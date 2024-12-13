# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root) -> int:
        depth = 0
        queue = [root]
        if not root:
            return depth
        
        while queue:
            le = len(queue)
            
            while le > 0:
                curr = queue.pop(0)
                le -= 1
                
                if not curr.left and not curr.right:
                    return depth +1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            depth += 1
        return depth
        
        