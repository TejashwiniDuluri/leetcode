# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        tortoise, hair = head, head

        if (not head) or not (head.next):
            return True

        stack = []
        while (hair and hair.next):
            stack.append(tortoise.val)
            tortoise = tortoise.next
            hair = hair.next.next

        if hair:
            tortoise = tortoise.next

        # NOW TORTOISE Is MID ELEM
        print(tortoise.val, hair.val, stack)
        while (tortoise):
            if not (stack.pop() == tortoise.val):
                return False
            tortoise = tortoise.next
        return not stack


# 1,2,2,1

# stack = [1,2]
# tortoise => 2
# hair => None

head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
head = ListNode(1, ListNode(2))
head = ListNode(1, ListNode(0, ListNode(1)))

obj = Solution()
print(obj.isPalindrome(head))
