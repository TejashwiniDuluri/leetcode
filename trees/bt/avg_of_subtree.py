# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.count = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.avg(root, 0, 0)
        return self.count

    def avg(self, root, summ, count):

        summ += root.val
        count += 1

        if root.left:
            node, childs_summ, childs_count = self.avg(root.left, 0, 0)
            summ += childs_summ
            count += childs_count

        if root.right:
            node, childs_summ, childs_count = self.avg(root.right, 0, 0)
            summ += childs_summ
            count += childs_count

        avg = summ // count
        if root.val == avg:
            self.count += 1

        return root, summ, count
