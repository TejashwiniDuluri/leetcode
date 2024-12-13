# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.result = []
        self.length = 0
        
    def getMinimumDifference(self, root) -> int:
        
        self.inorder(root)
        mini = abs(self.result[0] - self.result[1])
        
        i,j = 1,2
        while j < self.length:
            mini = min(mini, abs(self.result[i] - self.result[j]) )
            i+=1
            j+=1
        return mini
            
        
        
    def inorder(self, root):
        
        if root:
            self.inorder(root.left)
            self.result.append(root.val)
            self.length+=1
            self.inorder(root.right)
        return 