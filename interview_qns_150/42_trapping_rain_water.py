from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # first see what is left max level at each height
        # see what is right max level at each height
        # remember its not exactly neighbour but till first to last
        # now your level is min(left_max, right_max) as even if one is too big other also should support to store water
        # and suppose if your left is 3 and right is 5 and current height is 1 => as min is 3 your rain water is not 3 as there is a height of 1 upwards so negate the height also
        # finally its min(left_max, right_max) - height => and consider this only if its positive and if its negative ignore

        # left_max_array = [0]
        # right_max_array = [0]

        # height_len = len(height)
                
        # for i in range(1, height_len):
        #     left_max_array.append(max(height[i-1], left_max_array[-1]))

        # for i in range(height_len-2, -1, -1):   
        #     right_max_array.insert(0, max(height[i+1], right_max_array[0]))            

        # rain_water = 0
        # index = 0
        # for left_max, right_max in zip(left_max_array, right_max_array) :
        #     res = min(left_max, right_max) - height[index]
        #     rain_water += res if res > 0 else 0           
        #     index+=1
        
        # return rain_water

        # ====== optimized solution - two pointers ========
        
        heights_len = len(height)
        left_max = 0
        right_max = 0
        left = 0
        right = heights_len-1
        ans = 0

        while left < right:

            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left+=1
            else:
                right_max = max(right_max,height[right])
                ans += right_max - height[right]
                right -=1
        return ans

        

height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution()
print(obj.trap(height))
        