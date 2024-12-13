from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        i = 0
        j = len(nums)-1
        
        count = 0
        
        while i < j:
            summ = nums[i] + nums[j]
            if summ < target:
                count += j-i
                i+=1
            else:
                j-=1                
        return count

nums = [-6,2,5,-2,-7,-1,3]
target = -2
# nums = [-1,1,2,3,1]
# target = 2
obj = Solution()
print(obj.countPairs(nums, target))