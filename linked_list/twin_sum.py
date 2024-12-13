# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head) -> int:
        tortoise = head
        hair = head.next

        stack = [tortoise.val]
        while (hair and hair.next):
            tortoise = tortoise.next
            stack.append(tortoise.val)
            hair = hair.next.next

        tortoise = tortoise.next
        twin_sum = 0
        while (tortoise):

            twin_sum = max(twin_sum, stack.pop() + tortoise.val)
            tortoise = tortoise.next

        return twin_sum


head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
head = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
head = ListNode(1, ListNode(100000))
obj = Solution()
print(obj.pairSum(head))
