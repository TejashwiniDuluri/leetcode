# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        root = self._delete(root, key)
        return root

    def _delete(self, root, key):
        if not root:  # if does not found
            return root

        elif key < root.val:
            root.left = self._delete(root.left, key)

        elif key > root.val:
            root.right = self._delete(root.right, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ = self.inorder_successor(root)
                root.val = succ.val
                root.right = self.deleteNode(root.right, root.val)

        return root

    def inorder_successor(self, root):

        curr = root.right
        while curr.left:
            curr = curr.left
        return curr.val
