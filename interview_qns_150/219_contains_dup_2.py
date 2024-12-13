from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        for index, val in enumerate(nums):
            if val in hash_map and abs( index-hash_map[val]) <= k:
                return True
            
            hash_map[val] = index
        return False


obj = Solution()
nums = [1,2,3,1]
k = 3
nums = [1,2,3,1,2,3]
k = 2
print(obj.containsNearbyDuplicate(nums, k))
        