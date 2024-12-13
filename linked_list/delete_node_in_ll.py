# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # curr = node
        # while curr.next:
        #     next = curr.next
        #     curr.val = next.val
        #     if next:
        #         curr = curr.next
        #     else:
        #         curr.next = None
        # return curr
        
        ### optimized to below ####
        node.val = node.next.val
        node.next = node.next.next
        
    