# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_max(self, array):
        max_val = array[0]
        max_ind = 0
        for ind, val in enumerate(array):
            if val > max_val:
                max_ind = ind
                max_val = val

        left = array[0:max_ind]
        right = array[max_ind+1:]
        return max_val, left, right

    def constructMaximumBinaryTree(self, nums):

        max_val, left, right = self.find_max(nums)

        root = TreeNode(max_val)

        if left:
            root.left = self.constructMaximumBinaryTree(left)
        if right:
            root.right = self.constructMaximumBinaryTree(right)

        return root
