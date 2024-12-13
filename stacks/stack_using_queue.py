class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for i in range(len(self.q1)-1):
            elem = self.q1.pop(0)
            self.q2.append(elem)

        elem = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        # print(self.q1, self.q2)

        return elem

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        # if len(self.q1) == 0:
        #     return True
        # return False
        # print(self.q1, self.q2)
        return not self.q1


obj = MyStack()
print(obj.push(1))
print(obj.push(2))
print(obj.top())
print(obj.pop())
# print(obj.pop())
print(obj.empty())
