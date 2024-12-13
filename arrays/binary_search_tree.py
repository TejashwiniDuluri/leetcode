
# Implementation of a binary search tree
class BST:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val == None:
            self.val = val
            return
        if val == self.val:
            return
        if val < self.val:
            # left does not exist
            if self.left == None:
                self.left = BST(val)
            else:
                self.left.insert(val)
            return
        if val > self.val:
            if self.right == None:
                self.right = BST(val)
            else:
                self.right.insert(val)
            return

    def search(self, val):
        if self.val == val:
            return True
        elif val < self.val:
            if self.left == None:
                return False
            self.left.search(val)
        elif val > self.val:
            if self.right == None:
                return False
            self.right.search(val)
        else:
            return False

    def inorder(self, result=[]):
        # left,val,right
        if self.left is not None:
            self.left.inorder(result)
        if self.val is not None:
            result.append(self.val)
        if self.right is not None:
            self.right.inorder(result)
        return result

    def preorder(self, result=[]):
        # value, left, right
        if self.val is not None:
            result.append(self.val)
        if self.left is not None:
            self.left.preorder(result)
        if self.right is not None:
            self.right.preorder(result)
        return result

    def postorder(self, result=[]):
        # left, right, value
        if self.left is not None:
            self.left.postorder(result)
        if self.right is not None:
            self.right.postorder(result)
        if self.val is not None:
            result.append(self.val)
        return result


tree = BST()
nums = [-10, -3, 0, 5, 9]

for i in nums:
    tree.insert(i)


########################################


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val == None:
            self.val = val
            return
        if val == self.val:
            return
        if val < self.val:
            # left does not exist
            if self.left == None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
            return
        if val > self.val:
            if self.right == None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
            return


class Solution:

    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        tree = TreeNode(nums[mid])
        tree.insert(nums[mid])
        left = nums[:mid]
        right = nums[mid+1:]
        self.sortedArrayToBST(left)
        self.sortedArrayToBST(right)
        return tree


nums = [1, 3]
Solution().sortedArrayToBST(nums)
