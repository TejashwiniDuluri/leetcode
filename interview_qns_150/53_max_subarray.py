from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float("-inf")
        curr_sum = 0

        for i in nums:
            curr_sum = max(curr_sum + i, i)
            max_sum = max(curr_sum, max_sum)
            print(curr_sum, max_sum)
        return max_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1, -1,2,3,5,1]
obj = Solution()
print(obj.maxSubArray(nums))