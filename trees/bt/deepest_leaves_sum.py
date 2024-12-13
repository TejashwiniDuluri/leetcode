# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root) -> int:

        # queue = [root]

        # level_sum = 0

        # while queue:

        #     queue_len = len(queue)
        #     level_sum = 0

        #     while queue_len > 0:

        #         node = queue.pop(0)
        #         queue_len -= 1

        #         level_sum += node.val

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return level_sum

        ###
        if not root:
            return 0

        dq = deque([root])
        level_sum = 0

        while dq:

            level_sum = 0
            queue_len = len(dq)

            while queue_len > 0:

                node = dq.popleft()
                queue_len -= 1
                level_sum += node.val

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return level_sum
