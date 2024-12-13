from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        nums_len = len(nums)
        result = [1]*nums_len
        for i in range(nums_len):

            for j in range(i):
                
                if nums[j] < nums[i]:
                    result[i] = max(result[j] +1, result[i]) 
            print(result)
        return max(result)


        
obj = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = [1,2,3,4]
nums = [0,1,0,3,2,3]
nums = [0,1,0,3]
print(obj.lengthOfLIS(nums))