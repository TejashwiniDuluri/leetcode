from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix_prod = 1  
        suffix_prod = 1
        result = max(nums)
        nums_len = len(nums)

        for ind, val in enumerate(nums):
            
            prefix_prod *= val
            result = max(result, prefix_prod)

            if prefix_prod == 0:
                prefix_prod =1

            suffix_prod *= nums[nums_len-1-ind]
            result = max(result, suffix_prod)
            if suffix_prod == 0:
                suffix_prod = 1

        return result



obj = Solution()
nums = [2,3,-2,4]
# nums =[-2,0,-1]
# nums =[-2,3,-4]
print(obj.maxProduct(nums))