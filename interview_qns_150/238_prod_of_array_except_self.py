from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        right_prod = 1
        
        results = [0] * len(nums)
                
        for index, i in enumerate(nums):
            results[index] = left_prod
            left_prod *= i        
        for index in range(len(nums)-1, -1 , -1):            
            results[index] *= right_prod 
            right_prod *= nums[index]
        
        return results
    
obj = Solution()
nums = [1,2,3,4]
print(obj.productExceptSelf(nums))


