import math

# ========== average coders do============
# class ProductOfNumbers:

#     def __init__(self):
#         self.array = []

#     def add(self, num: int) -> None:
#         self.array.append(num)
#         return None

#     def getProduct(self, k: int) -> int:
#         return math.prod(self.array[-k:])


class ProductOfNumbers:

    def __init__(self):
        self.array = [1]

    def add(self, num: int) -> None:
        
        if num:            
            self.array.append(self.array[-1]*num)
        else:
            self.array = [1]
        
        return None

    def getProduct(self, k: int) -> int:
        
        if len(self.array) <= k:
            return 0
        
        return self.array[-1]//self.array[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:


["ProductOfNumbers", "add", "add", "add", "add", "add",
    "getProduct", "getProduct", "getProduct", "add", "getProduct"]

[[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]

obj = ProductOfNumbers()

print(obj.add(3))
print(obj.array)
print(obj.add(0))
print(obj.array)
print(obj.add(2))
print(obj.add(5))
print(obj.add(4))
print(obj.array)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
print(obj.add(8))
print(obj.getProduct(2))
