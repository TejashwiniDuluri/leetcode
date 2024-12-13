
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head:
            curr = self.head
            new_node.next = curr
            self.head = new_node
        else:
            self.head = new_node
            return

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.next = new_node
        return

    def traverse(self, obj):
        current = obj.head
        li = []
        while (current):
            li.insert(0, current.val)
            current = current.next
        return li

    def addTwoNumbers(self, l1, l2):
        # l1_data = self.traverse(l1)
        # l2_data = self.traverse(l2)

        # sum = int(",".join([str(i) for i in l1_data]).replace(
        #     ",", ""))+int(",".join([str(i) for i in l2_data]).replace(",", ""))

        # l3 = Solution()
        # for i in str(sum):
        #     l3.addAtHead(int(i))

        # return l3

        l1_data = []
        l2_data = []

        current = l1
        while (current.next):
            l1_data.insert(0, current.val)
            current = current.next
        l1_data.insert(0, current.val)

        current = l2
        while (current.next):
            l2_data.insert(0, current.val)
            current = current.next
        l2_data.insert(0, current.val)

        sum = int(",".join([str(i) for i in l1_data]).replace(
            ",", ""))+int(",".join([str(i) for i in l2_data]).replace(",", ""))

        str_sum = str(sum)[::-1]
        
        print(l1_data, l2_data, sum, str_sum)

        l3 = ListNode(str_sum[0])
        current = l3
        for i in range(1, len(str_sum)):

            current.next = ListNode(str_sum[i])
            current = current.next
        return l3
    
        # temp = dummy
        # while (temp):
        #     print(temp.val)
        #     temp = temp.next
        # return dummy


obj = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))


l3 = obj.addTwoNumbers(l1, l2)
