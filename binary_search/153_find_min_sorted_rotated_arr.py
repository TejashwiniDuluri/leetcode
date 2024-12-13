from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:
        nums_len = len(nums)
        low = 0
        high = nums_len - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                low = mid + 1 
            else:
                high = mid

        return nums[low]

        
          
obj = Solution()
nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
print(obj.findMin(nums))