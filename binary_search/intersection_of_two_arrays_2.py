from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []

        nums1_dict = {}
        for i in nums1:
            if nums1_dict.get(i):
                nums1_dict[i] += 1
            else:
                nums1_dict[i] = 1

        for val in nums2:
            if val in nums1_dict and nums1_dict[val]>0:
                result.append(val)
                nums1_dict[val] -=1
        
        return result

        


nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
print(obj.intersect(nums1, nums2))
        
