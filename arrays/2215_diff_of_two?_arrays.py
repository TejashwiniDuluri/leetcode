from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        result = [[], []]

        result[0] = list(set(nums1).difference(set(nums2)))
        result[1] = list(set(nums2).difference(set(nums1)))
        return result

obj = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
print(obj.findDifference(nums1, nums2))
        