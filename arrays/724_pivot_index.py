from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_pref = [0]
        right_pref = 0

        index = -1

        for i in range(len(nums) - 1):
            left_pref.append(left_pref[-1] + nums[i])
        for i in range(len(nums)-1, -1, -1):   
            # print(left_pref[i], right_pref + nums[i])
            if left_pref[i] ==  right_pref:
                index =  i
            right_pref = right_pref + nums[i]

        return index
        
obj = Solution()
nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
print(obj.pivotIndex(nums))


