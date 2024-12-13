from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # result = []

        # nums1_dict = {}
        # for i in nums1:
        #     nums1_dict[i] = i
        
        # nums2_dict = {}
        # for i in nums2:
        #     nums2_dict[i] = i

        # for i in nums1_dict:
        #     if nums2_dict.get(i) != None:
        #         result.append(i)
        
        # return result
    
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = nums1.intersection(nums2)
        return list(result)

nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
print(obj.intersection(nums1, nums2))
        