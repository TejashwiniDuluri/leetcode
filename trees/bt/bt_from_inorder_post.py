# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.index = -1

    def buildTree(self, inorder, postorder):
        root = TreeNode(postorder[self.index])

        left, right = self.find_target(postorder, inorder)
        self.index += 1
        if left:
            root.left = self.buildTree(left, postorder)
        if right:
            root.right = self.buildTree(right, postorder)

        return root

    def find_target(self, postorder, array):

        for ind, val in enumerate(array):
            if val == postorder[self.index]:
                left = array[0:ind]
                right = array[ind+1:]
                return left, right
        return [], []
