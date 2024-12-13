# Definition for a binary tree node.

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root) -> Optional[TreeNode]:

        dq = deque([root])
        parent_dict = {}

        while dq:

            dq_len = len(dq)
            level_nodes = dq.copy()

            while dq_len > 0:
                
                node = dq.popleft()
                dq_len -= 1

                if node.left:
                    dq.append(node.left)
                    parent_dict[node.left] = node
                if node.right:
                    dq.append(node.right)
                    parent_dict[node.right] = node

            
        while len(level_nodes) > 1: # ==1 case is found the parent root node
            level_nodes = set(parent_dict[node] for node in level_nodes) 
        
        return level_nodes.pop()



        