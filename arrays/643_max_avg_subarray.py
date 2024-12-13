
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        i = 0
        curr_sum = 0
        max_avg = float("-inf")        
    
        while i < k:
            curr_sum += nums[i]
            i+=1

        max_avg = max(curr_sum/k, max_avg)

        while i < len(nums):            
            curr_sum = curr_sum + nums[i] - nums[i-k]            
            max_avg = max(curr_sum/k, max_avg)
            i+=1            
        
        return max_avg


obj = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
nums = [5]
k = 1
# nums =[0,1,1,3,3]
# k = 4
print(obj.findMaxAverage(nums, k))
        