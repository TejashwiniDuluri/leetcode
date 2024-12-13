class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = []
        self.queue_len = 0

    def enQueue(self, value: int) -> bool:
        if self.queue_len == self.size:
            return False
        else:
            self.queue.append(value)
            self.queue_len += 1
            return True

    def deQueue(self) -> bool:
        if self.queue_len == 0:
            return False
        else:
            self.queue.pop(0)
            self.queue_len -= 1
            return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[0]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[-1]

    def isEmpty(self) -> bool:
        return self.queue_len == 0

    def isFull(self) -> bool:
        return self.queue_len == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# k = 3
# obj = MyCircularQueue(k)
# print(obj.enQueue(1))
# print(obj.enQueue(2))
# print(obj.enQueue(3))
# print(obj.enQueue(4))
# print(obj.Rear())
# print(obj.isFull())
# print(obj.deQueue())
# print(obj.enQueue(4))
# print(obj.Rear())


########
obj = MyCircularQueue(8)
print(obj.enQueue(3))
print(obj.enQueue(9))
print(obj.enQueue(5))
print(obj.enQueue(0))
print(obj.deQueue())
print(obj.deQueue())
print(obj.isEmpty())
print(obj.isEmpty())
print(obj.Rear())
print(obj.Rear())
print(obj.deQueue())
