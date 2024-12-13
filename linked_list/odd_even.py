# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        # This preseves head so off head you can make changes
        if not head:
            return head
        odd = head

        even = odd.next
        even_head = even

        while (even and even.next):
            print(odd.val, even.val)
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head


head = [1, 2, 3, 4, 5]
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
s.oddEvenList(ll)
