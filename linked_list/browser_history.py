

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str):
        if not self.head:
            self.head = ListNode(url)
            self.current = self.head
        else:

            new_node = ListNode(url)
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node
        return None

    def back(self, steps: int):
        present = self.current
        if not present.prev:
            return present.val

        step = 1

        while step <= steps and present:

            present = present.prev

            if present:
                self.current = present

            if not present:
                return self.current.val
            step = step+1
        self.current = present
        return present.val

    def forward(self, steps: int):
        present = self.current

        if not present.next:
            return self.current.val

        step = 1
        while step <= steps and present:
            present = present.next
            if present:
                self.current = present

            if not present:
                return self.current.val

            step = step+1
        self.current = present
        return present.val

    def traverse(self):
        curr = self.head
        while curr.next:
            print(curr.val)
            curr = curr.next
        print(curr.val)


# obj = BrowserHistory("leetcode.com")
# print(obj.visit("google.com"))
# print(obj.visit("facebook.com"))
# print(obj.visit("youtube.com"))
# # obj.traverse()
# print(obj.back(1))
# print(obj.back(1))
# print(obj.forward(1))
# print(obj.visit("linkedin.com"))
# print(obj.forward(2))
# print(obj.back(2))
# print(obj.back(7))


# ["BrowserHistory", "visit", "visit", "visit", "back",
#     "back", "forward", "visit", "forward", "back", "back"]
# [["leetcode.com"], ["google.com"], ["facebook.com"], [
#     "youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]
# [None, None, None, None, "facebook.com", "google.com", "facebook.com",
#     None, "linkedin.com", "google.com", "leetcode.com"]


["BrowserHistory", "visit", "back", "back",
    "forward", "forward", "visit", "visit", "back"]

obj = BrowserHistory("zav.com")
print(obj.visit("kni.com"))
print(obj.back(7))
print(obj.back(7))
print(obj.forward(5))
print(obj.forward(1))
print(obj.visit("pwrrbnw.com"))
print(obj.visit("mosohif.com"))
print(obj.back(9))


[["zav.com"], ["kni.com"], [7], [7], [5], [
    1], ["pwrrbnw.com"], ["mosohif.com"], [9]]
[None, None, "zav.com", "zav.com", "kni.com", "kni.com", None, None, "zav.com"]
