# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self):
    #     self.index = 0
    #     self.root = None
    #     self.preorder = None
    #     self.inorder = None

    # def buildTree(self, preorder, inorder):
    #     self.preorder = preorder
    #     self.inorder = inorder
    #     root = TreeNode(preorder[self.index])
    #     self.index += 1
    #     val, left, right = self.find_target(inorder)
    #     root.left = self.construct_tree(left)
    #     root.right = self.construct_tree(right)
    #     return self.root

    # def find_target(self, inorder):
    #     for ind, val in enumerate(inorder):
    #         if ind == self.index:
    #             left_array = inorder[0:ind]
    #             right_array = inorder[ind+1:]
    #             return val, left_array, right_array

    # def construct_tree(self, array):
    #     val, left, right = self.find_target(array)
    #     node = TreeNode(val)
    #     if left:
    #         node.left = self.construct_tree(left)
    #     if right:
    #         node.right = self.construct_tree(right)
    #     return node

    def __init__(self):
        self.index = 0

    def buildTree(self, preorder, inorder):

        root = TreeNode(preorder[self.index])
        left, right = self.find_target(preorder, inorder)
        self.index += 1
        if left:
            root.left = self.buildTree(left, preorder, inorder)
        if right:
            root.right = self.buildTree(right, preorder, inorder)
        return root

    def find_target(self, preorder, inorder):

        for ind, val in enumerate(inorder):
            if val == preorder[self.index]:
                left_array = inorder[0:ind]
                right_array = inorder[ind+1:]
                return val, left_array, right_array

        return [], []
