
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head):
        # works for unique array of elements

        tail = head
        stack = []
        results = {}
        index = 0

        while tail:
            while stack and int(stack[-1].split("-")[1]) < tail.val:
                results[stack.pop()] = tail.val
            results[f"{index}-{tail.val}"] = 0
            stack.append(f"{index}-{tail.val}")
            tail = tail.next
            index = index+1
        while stack:
            results[stack.pop()] = 0

        return list(results.values())


obj = Solution()
head = [2, 7, 4, 3, 5]
ll = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))

# head = [2, 1, 5]
# ll = ListNode(2, ListNode(1, ListNode(5)))
print(obj.nextLargerNodes(ll))
