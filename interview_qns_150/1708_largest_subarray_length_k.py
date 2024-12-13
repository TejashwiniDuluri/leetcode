from typing import List

class Solution:
    def max_subarray_len_k(self, nums: List[int], k) -> int:
        
        curr_sum =  0

        start = 0
        end = len(nums) 
        k_end = start + k 
        
        for ind in range(k_end):
            curr_sum+=nums[ind]
        
        max_sum = curr_sum

        for ind in range(k_end, end):
            curr_sum -= nums[start]
            curr_sum += nums[ind]
            max_sum = max(curr_sum, max_sum)
            start +=1

        return max_sum


obj = Solution()
print(obj.max_subarray_len_k([1,2,3,4,5,6,7,8,9,10], 1))
        