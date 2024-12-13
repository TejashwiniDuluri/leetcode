from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        while left < right:
            val = numbers[left] + numbers[right]
            if  val == target:
                return [left+1, right+1]
            elif val < target:
                left +=1
            else:
                right -= 1

obj = Solution()
numbers = [2,7,11,15]
target = 9
numbers = [2,3,4]
target = 6
numbers = [-1,0]
target = -1
print(obj.twoSum(numbers, target))
        