from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:


        prefix = 0
        max_alt = 0

        for i in gain:
            max_alt = max(max_alt, prefix + i)
            prefix = prefix + i
        return max_alt



obj = Solution()
gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
print(obj.largestAltitude(gain))
        