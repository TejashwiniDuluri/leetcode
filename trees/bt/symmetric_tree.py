
# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSymmetric(self, root) -> bool:

        # dq = deque([root])

        # while dq:

        #     dq_len = len(dq)

        #     level_elements = []

        #     while dq_len > 0:

        #         node = dq.popleft()
        #         dq_len -= 1
                
        #         if not node:
        #             level_elements.append(None)
        #             continue
        #         else:
        #             level_elements.append(node.val)

        #         level_elements.append(node.val)
                
        #         dq.append(node.left)
        #         dq.append(node.right)
                
        #     if level_elements != level_elements[::-1]:
        #         return False
        # return True
                
        ########### DFS ############

        status = True

        def traverse(node1, node2):

            nonlocal status

            if not node1 and not node2:
                return 
            if (node1 and node2 and node1.val != node2.val) or (node1 or node2):
                status = False
                return 
            
            traverse(node1.left, node2.right)
            traverse(node1.right, node1.left)
        
        traverse(root.left, root.right)
        return status









     