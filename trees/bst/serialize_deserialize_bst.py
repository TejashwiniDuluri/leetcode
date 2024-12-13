# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        string = ""

        def convert_to_str(node):
            nonlocal string
            if not node:
                return

            string = string + str(node.val) + "-"

            if node.left:
                convert_to_str(node.left)

            if node.right:
                convert_to_str(node.right)

        convert_to_str(root)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """

        if not data:
            return []

        data = list(map(int, data.strip("-").split("-")))
        root = TreeNode(data.pop(0))

        for i in data:
            self.insert(root, i)

        return root

    def insert(self, node, value):
        if not node:
            return TreeNode(value)

        if value < node.val:
            node.left = self.insert(node.left, value)
        if value > node.val:
            node.right = self.insert(node.right, value)

        return node
