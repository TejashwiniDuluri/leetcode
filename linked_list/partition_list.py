# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        pass


[1, 4, 3, 2, 5, 2]
head = ListNode(1, ListNode(4, ListNode(
    3, ListNode(2, ListNode(5, ListNode(2))))))
ll = Solution()
ll.partition(head)
