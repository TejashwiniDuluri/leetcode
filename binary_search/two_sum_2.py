from typing import Optional, List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # =====two pointers approach
        # i = 0
        # j = len(numbers)-1        

        # while i<j:
        #     summ = numbers[i] + numbers[j]
        #     if summ == target:
        #         return [i+1, j+1]
            
        #     if summ > target:
        #         j-=1
        #     else:
        #         i+=1
        
        # binary search approach

        

        
obj = Solution()
numbers = [2,3,4]
target = 6
# numbers = [2, 7, 11, 15]
# target = 9
print(obj.twoSum(numbers, target))