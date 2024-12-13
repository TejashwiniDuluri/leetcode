# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root) :
        
        level = 0
        dq = deque([root])

        while dq:

            queue_len = len(dq)


            while queue_len > 0:

                node = dq.popleft()
                
                queue_len -= 1

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            level += 1

            if level % 2 != 0:

                dq_len = len(dq)

                for i in range( dq_len//2 ):
                    dq[i].val,dq[-i-1].val = dq[-i-1].val,dq[i].val
            
        return root




                






        