

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def sort_array(self, nums):
        mid = len(nums) // 2
        # print(mid)
        root = TreeNode(nums[mid])
        print(root.val, root.left, root.right)
        root.left = self.sort_array(nums[:mid])
        root.right = self.sort_array(nums[mid+1:])

        return root


nums = [-10, -3, 0, 5, 9]
obj = BinarySearchTree()
print(obj.sort_array(nums))
