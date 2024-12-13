from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_level = 0
        left = 0
        right = len(height) - 1
        while left < right:            
            curr_level = abs(left - right) * min(height[right], height[left])
            max_level  = max(max_level, curr_level)
            
            if height[left] < height[right]:
                left +=1
            else:
                right-=1
        return max_level


        
height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
obj = Solution()
print(obj.maxArea(height))