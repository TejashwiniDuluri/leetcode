from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        for index , val in enumerate(nums):            
            if target - val in hash_map:                
                return [hash_map.get(target - val), index]
            hash_map[val] = index            
        return []
    
nums = [2,7,11,15]
target = 9
obj  = Solution()
print(obj.twoSum(nums, target))
        