# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def traverse(node, path_list):
            nonlocal count

            if not node:
                return

            if not path_list:
                count += 1
                path_list.append(node.val)
                print(node.val, "root")
            
            else:
                path_list.append(node.val)
                if node.val >= max(path_list):
                    count += 1
                    print(node.val, "else")
            
            path_list = path_list.copy()
            if node.left:
                traverse(node.left, path_list)
            if node.right:
                traverse(node.right, path_list)

            return node

        traverse(root, [])
        return count

    # ======================
        count = 0

        def traverse(node, max_value):
            nonlocal count

            if not node:
                return

            if node.val >= max_value:
                count += 1
                max_value = node.val

            if node.left:
                traverse(node.left, max_value)
            if node.right:
                traverse(node.right, max_value)

            return node

        traverse(root, root.val)
        return count
