# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        # need to know length   
        length = 1
        tail = head

        while (tail.next):
            tail = tail.next
            length = length+1

        k = k % length

        curr = head
        for i in range(length - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        tail.next = head

        return new_head


ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2

obj = Solution()
obj.rotateRight(ll, k)
