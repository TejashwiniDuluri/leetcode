# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        # finding middle element and last node
        tortoise = head
        hair = head.next

        while hair and hair.next:
            tortoise = tortoise.next
            hair = hair.next.next

        # reverse list from middle next to last
        current = tortoise
        prev = None

        while (current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        print("===head====")
        t = head
        while (t):
            print(t.val)
            t = t.next
        print("===prev====")

        t = prev
        while (t):
            print(t.val)
            t = t.next

        t_start = head
        p_start = prev
        while (t_start):
            t_next = t_start.next
            p_next = p_start.next
            t_start.next = p_start
            p_start.next = t_next

            t_start = t_next
            p_start = p_next

        print("==final ")
        t = head
        while (t):
            print(t.val)
            t = t.next


[1, 2, 3, 4, 5]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
print(obj.reorderList(head))
