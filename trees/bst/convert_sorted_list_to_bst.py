# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def __init__(self):
#         self.root = None

#     def sortedListToBST(self, head) :
#         nodes_list = []
#         tail = head
#         while tail:
#             nodes_list.append(tail.val)
#             tail = tail.next
        
#         self.pick_elements(nodes_list)
#         return self.root

#     def pick_elements(self, nums):
#         if not nums:
#             return None
        
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid+1:]

#         if not self.root:
#             self.root = TreeNode(nums[mid])
#         else:
#             self.insert(self.root, nums[mid])
        
#         self.pick_elements(left)
#         self.pick_elements(right)

#         return self.root
    
#     def insert(self, root, val):
        
#         if not root:
#             return TreeNode(val)
        
#         if val < root.val:
#             root.left = self.insert(root.left, val)
#         elif val > root.val:
#             root.right = self.insert(root.right, val)

#         return root

##############


class Solution:    

    def sortedListToBST(self, head) :
        nodes_list = []
        tail = head
        while tail:
            nodes_list.append(tail.val)
            tail = tail.next
        
        return self.pick_elements(nodes_list)
        

    def pick_elements(self, nums):
        if not nums:
            return None
        
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid+1:]
        
        root = TreeNode(nums[mid])
        
        root.left = self.pick_elements(left)
        root.right = self.pick_elements(right)

        return root




    
    

        