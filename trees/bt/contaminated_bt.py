# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hash = {}
        self.root = self.recover_tree(root, 0)

    def recover_tree(self, root, val):
        if root:
            root.val = val
            self.hash[val] = val

        if root.left:
            self.recover_tree(root.left, 2 * root.val + 1)

        if root.right:
            self.recover_tree(root.right, 2 * root.val + 2)

    def find(self, target: int) -> bool:
        return self.hash.get(target) == target

        # Your FindElements object will be instantiated and called as such:
        # obj = FindElements(root)
        # param_1 = obj.find(target)