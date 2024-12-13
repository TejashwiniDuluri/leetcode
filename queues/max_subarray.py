class Solution:
    def maxSubArray(self, nums):
        
        curr_sum = 0
        max_sum = nums[0]
        
        for i in nums:
            curr_sum = i if i > curr_sum+i else curr_sum+i
            
            max_sum = curr_sum if curr_sum > max_sum else max_sum
        
        return max_sum
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
obj = Solution()
print(obj.maxSubArray(nums))