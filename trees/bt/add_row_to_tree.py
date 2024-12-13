# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root, val: int, depth: int) :
        
        dq = deque([root])

        level = 1

        if level == depth:
            new_node = TreeNode(val, root)
            return new_node
        
        while dq:

            queue_len = len(dq)

            while queue_len > 0:
                if level >= depth-1 :
                    break

                node = dq.popleft()
                queue_len -= 1

                if node.left:
                    dq.append(node.left)
                
                if node.right:
                    dq.append(node.right)

            if level >= depth-1:
                for node in dq:
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val,None, node.right)                                    
                break
            else:
                level += 1            
            
        return root

        