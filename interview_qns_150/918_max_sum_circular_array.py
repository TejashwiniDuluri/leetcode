from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # len_nums = len(nums)-1
        # curr_sum = 0
        # max_sum = float("-inf")
        # nums = nums+nums
        
        # for index, i in enumerate(nums):
        #     target = len_nums+index
        #     j=index
        #     while j<target:
        #         curr_sum = curr_sum+i
        #         max_sum = max(max_sum, curr_sum)
        #         j+=1
        #     curr_sum = 0
        # return max_sum
    
        # time taking process

        # a: apply kadane algorithm to find max sum
        # b: calculate min sum, total and max sum => calculate max sum by total- min sum

        curr_min_sum = float("inf")
        min_sum = float("inf")
        max_sum = float("-inf")
        curr_max_sum = float("-inf")
        total = 0

        for i in nums:

            total+=i

            curr_min_sum = min(curr_min_sum+i, i)
            min_sum = min(curr_min_sum, min_sum)

            curr_max_sum = max(i, curr_max_sum+i)
            max_sum = max(max_sum, curr_max_sum)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total-min_sum)

    

nums = [1,-2,3,-2]
# nums = [5,-3,5]
nums = [-3,-2,-3]
obj = Solution()
print(obj.maxSubarraySumCircular(nums))