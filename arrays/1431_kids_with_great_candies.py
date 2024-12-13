from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        
        max_ele = max(candies)
        
        result = []
        for i in candies:
            if i+extraCandies >= max_ele :
                result.append(True)
            else:
                result.append(False)

        return result


obj = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
candies = [4,2,1,1,2]
extraCandies = 1
candies = [12,1,12]
extraCandies = 10
# candies =[2,8,7]
# extraCandies =1
print(obj.kidsWithCandies(candies, extraCandies))