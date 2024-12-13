
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumEvenGrandparent(self, root: TreeNode) -> int:

        summ = 0

        def traverse(node, parent, grandparent):
            nonlocal summ

            if not node:
                return

            if grandparent and grandparent.val % 2 == 0:
                summ += node.val

            if node.left:
                traverse(node.left, node, parent)

            if node.right:
                traverse(node.right, node, parent)

        traverse(root, None, None)
        return summ

        ##########

        # summ = 0
        # path = []

        # def traverse(root, path):
        #     nonlocal summ

        #     path = path.copy()

        #     if not root:
        #         return

        #     if len(path) >= 2:
        #         gp = path[-2]
        #         if gp % 2 == 0:
        #             summ += root.val

        #     path.append(root.val)

        #     if root.left:
        #         traverse(root.left, path)

        #     if root.right:
        #         traverse(root.right, path)

        #     return root

        # traverse(root, [])
        # return summ

        # traverse(root, [])
        # return summ

        ##############
