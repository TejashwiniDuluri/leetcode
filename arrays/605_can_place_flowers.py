from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        potted = 0
        visited = False

        for i in flowerbed:
            if not visited and i == 0:
                potted += 1
                visited = True
            elif i == 1 and visited:
                potted -= 1                
            elif i == 1 and not visited:
                visited = True     
            else:
                visited = False

        return potted >= n



obj = Solution()
flowerbed = [1,0,0,0,1]
n = 1
flowerbed =[1,0,0,0,0,0,1]
n=2
flowerbed = [0,0,1,0,0]
n = 2
flowerbed =[1,0,0,0,0,1]
n = 2
flowerbed =[0,0,1,0,0]
n = 1
print(obj.canPlaceFlowers(flowerbed, n))