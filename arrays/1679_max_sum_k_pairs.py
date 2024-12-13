from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        hash = defaultdict(int)
                
        for i in nums:
            if k - i in hash and hash[k-i] > 0:
                hash[k-i] -= 1
                counter += 1
            else:
                hash[i] += 1
            
        return counter

        
obj = Solution()
nums = [1,2,3,4]
k = 5
# nums = [3,1,3,4,3]
# k = 6
nums =[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
k = 3
print(obj.maxOperations(nums, k))