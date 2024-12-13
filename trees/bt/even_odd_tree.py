# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root) -> bool:
        
        if not root:
            return True
        
        dq = deque([root])

        level = 0
        while dq:

            dq_len = len(dq)

            level_last_value = None

            while dq_len:

                node =  dq.popleft()  
                if (level %2 != 0 and (node.val %2 != 0 or (level_last_value and level_last_value <= node.val))) or (level %2 == 0 and (node.val %2 == 0 or (level_last_value and level_last_value >= node.val))):
                    return False
                                    
                dq_len -= 1
                    
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                
                level_last_value = node.val
            
            level +=1 

        return True
            

                



        