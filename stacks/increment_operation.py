
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.length = 0

    def push(self, x: int) -> None:
        if self.length != self.maxSize:
            self.stack.append(x)
            self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        else:
            self.length -= 1
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:

        if k <= self.length:
            index = k
        else:
            index = self.length

        for i in range(len(self.stack[0:index])):
            self.stack[i] = self.stack[i]+val


# Your CustomStack object will be instantiated and called as such:
stk = CustomStack(3)
stk.push(1)
stk.push(2)
stk.pop()
stk.push(2)
stk.push(3)
stk.push(4)
print(stk.increment(5, 100))
print(stk.increment(2, 100))
stk.pop()
stk.pop()
stk.pop()
