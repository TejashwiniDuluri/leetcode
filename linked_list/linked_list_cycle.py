# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):

        start = head
        end = head

        while (end.next):
            if start == end:
                return True
            else:
                start = start.next
                end = end.next.next
        return False


head = [3, 2, 0, -4]

head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
ll = Solution()
ll.hasCycle(head)
