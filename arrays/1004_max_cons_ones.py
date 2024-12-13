from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        max_count = 0
        
        left = 0
        zero_count = 0

        for right in range(len(nums)):
            
            if nums[right] == 0:
                zero_count +=1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_count = max(max_count, right - left + 1)
            
        return max_count



obj = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(obj.longestOnes(nums, k))
        