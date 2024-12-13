
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        
        zeros = 0
        
        max_window = 0

        for right in range(len(nums) ):
            
            if nums[right] == 0:
                zeros +=1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_window = max(max_window, right - left +1)
            right +=1
        return max_window-1

        
obj = Solution()
nums = [1,1,0,1]
# nums = [0,1,1,1,0,1,1,0,1]
nums = [1,1,1]
print(obj.longestSubarray(nums))