# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# For unsorted linked list, maintain a hashmap while traversing and see if current is duplicated.

class Solution:
    def deleteDuplicates(self, head):
        # current = head

        # while (current.next):
        #     if current.val == current.next.val:
        #         current.next = current.next.next
        #     current = current.next

        # tail = head
        # while (tail.next):
        #     print(tail.val)
        #     tail = tail.next
        # return head

        dummy = ListNode(0, head)
        current = dummy
        start = current.next
        if not start:
            return head
        end = start.next
        duplicate = None
        while (start):
            print(current.val, start.val, end, duplicate)
            if (not end) and (start.val != duplicate):
                current.next = start
                current = start
                break

            elif (not end) and (start.val == duplicate):
                break

            elif start.val == end.val:
                duplicate = start.val

            elif start.val != duplicate:
                current.next = start
                current = start

            start = start.next
            end = end.next

        current.next = None

        tail = dummy.next
        while (tail):
            print(tail.val)
            tail = tail.next
        return head


l = [1, 2, 3, 3, 4, 4, 5]
[1, 1, 1, 2, 3]
# head = ListNode(1, ListNode(2, ListNode(
#     3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))

head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
# head = ListNode(1, ListNode(1))
ll = Solution()
ll.deleteDuplicates(head)
