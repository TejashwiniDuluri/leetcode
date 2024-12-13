# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):

        new_head = ListNode(0)
        new_head.next = head
        curr = new_head.next

        elements = []

        while curr:
            elements.append(curr.val)
            curr = curr.next

        elements.sort()
        curr = new_head.next

        for i in elements:
            curr.val = i
            curr = curr.next

        return new_head.next
