# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head) :
        stack = []
        tail = head
        while tail:
            if not stack:
                stack.append(tail.val)
            else:
                while stack and tail.val > stack[-1]:
                    stack.pop()
                stack.append(tail.val)                
            tail = tail.next
        
        dummy = ListNode(0)  
        curr = dummy  
        for i in stack:            
            curr.next = ListNode(i)
            curr = curr.next
                           
        return dummy.next
        
            

head = [5,2,13,3,8]
head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
obj = Solution()
obj.removeNodes(head)        