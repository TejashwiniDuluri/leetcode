class Solution:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def push(self, elem):
        self.stack.append(elem)

    def calPoints(self, operations):

        for i in operations:
            if i == "C":
                self.pop()
            elif i == "D":
                if self.peek():
                    self.push(2 * self.peek())
            elif i == "+":
                self.push(sum(self.stack[-2:]))
            else:
                self.push(int(i))
        return sum(self.stack)


obj = Solution()
ops = ["5", "2", "C", "D", "+"]
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
ops = ["1", "C"]
print(obj.calPoints(ops))
