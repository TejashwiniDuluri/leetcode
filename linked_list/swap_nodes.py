# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        point = dummy
        swap1 = point.next
        if not swap1:
            return dummy.next

        swap2 = swap1.next
        if not swap2:
            return dummy.next

        while (swap1.next):
            print(point.val, swap1.val, swap2.val)
            swap1.next = swap2.next
            swap2.next = swap1
            point.next = swap2

            if not swap1.next:
                break
            point = swap1
            swap1 = point.next
            swap2 = swap1.next
            print(point.val, swap1.val, swap2.val, "after")

        return dummy.next


[1, 2, 3, 4]
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
ll = ListNode(1)
obj = Solution()
obj.swapPairs(ll)
