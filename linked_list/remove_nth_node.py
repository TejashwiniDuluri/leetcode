# Definition for singly-linked list.

# sliding window
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        i_node = dummy
        j_node = dummy

        for i in range(n):
            j_node = j_node.next

        while (j_node.next):
            j_node = j_node.next
            i_node = i_node.next

        i_node.next = i_node.next.next

        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
obj.removeNthFromEnd(head, 2)
