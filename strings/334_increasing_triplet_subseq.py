from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # take first if its smaller than current and second is greater than current
        #if current is greater than curr then exists
        first = float("inf")
        second = float("inf")
        
        for i in nums:
            if i > second:
                return True
            if i < first and second > i:
                first = i
            if i > first:
                second = i
        return False
        
obj = Solution()
nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
# nums =[20,100,10,12,5,13]
# nums =[1,5,0,4,1,3]
# nums = [4,5,2147483647,1,2]
# nums =[1,5,0,4,1,3]
# nums = [1,2,0,3]
print(obj.increasingTriplet(nums))
