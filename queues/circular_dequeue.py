class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.dequeue = []
        self.dequeue_len = 0

    def insertFront(self, value: int) -> bool:
        if self.dequeue_len == self.size:
            return False
        self.dequeue.insert(0, value)
        self.dequeue_len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.dequeue_len == self.size:
            return False
        self.dequeue.append(value)
        self.dequeue_len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.dequeue.pop(0)
        self.dequeue_len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.dequeue.pop()
        self.dequeue_len -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.dequeue[0]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.dequeue[-1]

    def isEmpty(self) -> bool:
        return self.dequeue_len == 0

    def isFull(self) -> bool:
        return self.dequeue_len == self.size


# Your MyCircularDeque object will be instantiated and called as such:
myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))  # return True
print(myCircularDeque.insertLast(2))  # return True
print(myCircularDeque.insertFront(3))  # return True
print(myCircularDeque.insertFront(4))  # return False, the queue is full.
print(myCircularDeque.getRear())      # return 2
print(myCircularDeque.isFull())       # return True
print(myCircularDeque.deleteLast())   # return True
print(myCircularDeque.insertFront(4))  # return True
print(myCircularDeque.getFront())     # return 4
