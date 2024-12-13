import random
class RandomizedSet:

    def __init__(self):
        self.elements_with_indexes = {}
        self.elements = []
        self.elements_length = 0

    def insert(self, val: int) -> bool:
        if val in self.elements_with_indexes:            
            return False
        else:
            self.elements_with_indexes[val] = self.elements_length
            self.elements.append(val)
            self.elements_length += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.elements_with_indexes:
            # should not use this below line as  it is o(n)
            # so u need to move the lement to last and pop from list         
            index  = self.elements_with_indexes[val]
            last_element = self.elements[-1]
            
            self.elements[index] = last_element
            self.elements_with_indexes[last_element]  = index

            self.elements.pop()            
            del self.elements_with_indexes[val]
            
            self.elements_length -= 1

            return True
        return False
        
    def getRandom(self) -> int:
        
        return random.choice(self.elements)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(0))
print(obj.insert(1))
print(obj.remove(0))
print(obj.insert(2))
print(obj.remove(1))
print(obj.getRandom())


