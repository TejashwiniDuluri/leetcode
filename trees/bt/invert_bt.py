# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def invertTree(self, root) :

        if not root:
            return root

        dq = deque([root])

        while dq:

            dq_len = len(dq)

            while dq_len > 0:

                node = dq.popleft()
                dq_len -= 1

                node.left, node.right = node.right, node.left                
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        
        return root






        