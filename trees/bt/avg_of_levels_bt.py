# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):

        queue = [root]
        results = []

        while queue:

            level_list = []
            le = len(queue)

            while le > 0:
                elem = queue.pop()
                level_list.append(elem)
                le -= 1

                if elem.left:
                    level_list.append(elem.left)
                if elem.right:
                    level_list.append(elem.right)

            avg = sum(level_list)/len(level_list)
            results.append(avg)

        return results
