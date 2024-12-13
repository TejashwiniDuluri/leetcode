# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):

        slow = head
        fast = head

        if not head or not head.next:
            return head

        while (fast and fast.next):
            print(slow.val, fast.val)
            fast = fast.next.next

            if not fast or (fast and not fast.next):
                print(slow.next.val)
                return slow.next

            slow = slow.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

ll = Solution()
print(ll.middleNode(head))
