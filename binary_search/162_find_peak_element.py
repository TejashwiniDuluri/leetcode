
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 1 if nums[0] < nums[1] else 0
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right)//2

            if nums[mid - 1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return right
        

obj = Solution()
nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
nums = [1,2]
print(obj.findPeakElement(nums))