# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):

        # ============ stack approach =============
        # l2_stack = []
        # l2_tail = l2
        # while (l2_tail):
        #     l2_stack.append(l2_tail.val)
        #     l2_tail = l2_tail.next

        # l1_stack = []
        # l1_tail = l1
        # while (l1_tail):
        #     l1_stack.append(l1_tail.val)
        #     l1_tail = l1_tail.next

        # result_ll = None

        # carry = 0

        # while (l1_stack) or l2_stack:
        #     val = 0

        #     if l2_stack and l1_stack:
        #         val = l2_stack.pop() + l1_stack.pop() + \
        #             carry if carry else l2_stack.pop() + l1_stack.pop()
        #     elif l2_stack:
        #         val = l2_stack.pop() + carry if carry else l2_stack.pop()
        #     elif l1_stack:
        #         val = l1_stack.pop() + carry if carry else l1_stack.pop()

        #     if val >= 10:
        #         val = str(val)
        #         carry, val = int(val[0]), int(val[1])
        #     else:
        #         carry = 0

        #     if not result_ll:
        #         result_ll = ListNode(val)
        #     else:
        #         new_node = ListNode(val)
        #         new_node.next = result_ll
        #         result_ll = new_node

        # if carry != 0:
        #     new_node = ListNode(carry)
        #     new_node.next = result_ll
        #     result_ll = new_node

        # return result_ll

        # ==========reversing technique ================

        prev = None
        curr = l1

        while (curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        l1 = prev

        prev = None
        curr = l2
        while (curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        l2 = prev
        l1_ref, l2_ref = l1, l2

        result_ll = None
        carry = 0

        while (l1_ref) or l2_ref:
            val = 0

            if l1_ref and l2_ref:
                val = l1_ref.val + l2_ref.val + \
                    carry if carry else l1_ref.val + l2_ref.val
                l1_ref = l1_ref.next
                l2_ref = l2_ref.next

            elif l2_ref:
                val = l2_ref.val + carry if carry else l2_ref.val
                l2_ref = l2_ref.next

            elif l1_ref:
                val = l1_ref.val + carry if carry else l1_ref.val
                l1_ref = l1_ref.next

            if val >= 10:
                val = str(val)
                carry, val = int(val[0]), int(val[1])
            else:
                carry = 0

            if not result_ll:
                result_ll = ListNode(val)
            else:
                new_node = ListNode(val)
                new_node.next = result_ll
                result_ll = new_node

        if carry != 0:
            new_node = ListNode(carry)
            new_node.next = result_ll
            result_ll = new_node

        tail = result_ll
        while (tail):
            print(tail.val)
            tail = tail.next
        return result_ll


l1 = [7, 2, 4, 3]
l2 = [5, 6, 4]




l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))

l1 = ListNode(0)
l2 = ListNode(7, ListNode(3))

l1 = ListNode(5)
l2 = ListNode(5)

l1 = ListNode(1)
l2 = ListNode(9, ListNode(9))

obj = Solution()
print(obj.addTwoNumbers(l1, l2))


