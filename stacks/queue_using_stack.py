class MyQueue:

    def __init__(self):
        self.out_stack = []
        self.inp_stack = []

    def push(self, x: int) -> None:
        self.inp_stack.append(x)

    def pop(self) -> int:
        if self.out_stack:
            rem_elem = self.out_stack.pop()
        else:
            for i in range(len(self.inp_stack)):
                self.out_stack.append(self.inp_stack.pop())
            rem_elem = self.out_stack.pop()

        return rem_elem

    def peek(self) -> int:
        if not self.out_stack:
            for i in range(len(self.inp_stack)):
                self.out_stack.append(self.inp_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.inp_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())
