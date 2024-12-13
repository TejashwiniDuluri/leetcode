# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.current = None

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        if not root.left and not root.right:
            return root

        self.construct_tree(root)

    def construct_tree(self, node):
        if not node:
            return

        if not self.current:
            self.current = node

        left_tree = node.left
        right_tree = node.right

        self.current.left = None
        self.current.right = node
        self.current = self.current.right

        if left_tree:
            self.construct_tree(left_tree)
        if right_tree:
            self.construct_tree(right_tree)

        return node
