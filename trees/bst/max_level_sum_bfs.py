# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        max_level = 1
        max_sum = root.val
                
        queue = []
        queue.append(root)
        level = 1
        
        while queue:
            
            queue_len = len(queue)
            curr_level_sum = 0
            
            while queue_len > 0:
                node = queue.pop(0)
                curr_level_sum += node.val
                queue_len -= 1
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            if curr_level_sum > max_sum:
                max_level = level
                max_sum = curr_level_sum
            level += 1
            
        return max_level
            