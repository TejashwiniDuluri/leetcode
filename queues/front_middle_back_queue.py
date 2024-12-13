class FrontMiddleBackQueue:

    def __init__(self):
        self.size = 0
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        self.size+=1

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(self.size//2, val)
        self.size+=1

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.size+=1    
    
    def popFront(self) -> int:
        if self.size:
            self.size -=1
            return self.queue.pop(0) 
        else :
            return -1

    def popMiddle(self) -> int:
        if self.size:
            self.size -= 1 
            return self.queue.pop(self.size//2)  
            
        else:
            return -1
        

    def popBack(self) -> int:
        if self.size:
            self.size -= 1 
            return self.queue.pop()  
        else:
            return -1
        

q = FrontMiddleBackQueue()
print(q.pushFront(1))   # [1]
print(q.pushBack(2))    # [1, 2]
print(q.pushMiddle(3))  # [1, 3, 2]
print(q.pushMiddle(4))  # [1, 4, 3, 2]
print(q.popFront())     # return 1 -> [4, 3, 2]
print(q.popMiddle())    # return 3 -> [4, 2]
print(q.popMiddle())    # return 4 -> [2]
print(q.popBack())      # return 2 -> []
print(q.popFront())     # return -1 -> [] (The queue is empty)
 