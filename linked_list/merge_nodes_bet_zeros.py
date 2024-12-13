# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head):
        sum = 0
        new_list = ListNode(0)
        curr = new_list
        tail = head.next
        while (tail):
            sum += tail.val
            if tail.val == 0:                
                curr.next = ListNode(sum)
                curr = curr.next
                sum = 0
            tail = tail.next
        return new_list.next


ll = ListNode(0, ListNode(3, ListNode(1, ListNode(
    0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))

[0, 1, 0, 3, 0, 2, 2, 0]

ll = ListNode(0, ListNode(1, ListNode(0, ListNode(
    3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
obj = Solution()
print(obj.mergeNodes(ll))
