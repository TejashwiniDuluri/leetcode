# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def levelOrder(self, root) :        
        results = []
        
        if not root:
            return results
        
        
        queue = [root]        
        
        while queue:
            
            queue_len = len(queue)
            curr_level_list = []
            
            while queue_len > 0:
                node = queue.pop(0)
                curr_level_list.append(node.val)
                queue_len -= 1
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                    
            results.append(curr_level_list)
        return results
    

obj = Solution()
obj.levelOrder(root)
                




                
            
            
        
        
          
        
        
        