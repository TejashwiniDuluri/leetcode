from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # left= 0 
        # right = 0        
        # nums_len = len(nums)

        # min_array_size  = float("inf")
        # summ = nums[left]
        
        # while left <= right :
        #     if summ < target and right == nums_len-1:
        #         break

        #     elif summ < target:
        #         right+=1
        #         summ += nums[right]

        #     elif summ >= target:                
        #         min_array_size = min(right-left+1, min_array_size)
        #         summ -= nums[left]
        #         left+=1                                
        
        # return min_array_size if min_array_size != float("inf") else 0

            
        #or 
        total = 0
        i=0
        nums_len = len(nums)
        min_size = float("inf")

        for j in range(nums_len):
            total+=nums[j]

            while total >= target:
                min_size = min(min_size, j-i+1)
                total -= nums[i]
                i+=1

        return min_size if min_size != float("inf") else 0




        

obj = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(obj.minSubArrayLen(target, nums))