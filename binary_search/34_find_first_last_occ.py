from typing import List


class Solution:

    def first_occ(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                return mid
            
            elif nums[mid-1] == target and nums[mid-1] == target:
                high = mid-1                

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return mid if nums[mid] == target else -1

    def last_occ(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target and (mid == len(arr) - 1 or nums[mid+1] != target):
                return mid
            elif nums[mid] == target and nums[mid+1] == target:
                low = mid+1
                                
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return mid if nums[mid] == target else -1
        

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = self.first_occ(nums)
        last = self.last_occ(nums)
        return [first, last] 
  

obj = Solution()
nums = [5,7,7,8,8,10]
target = 8
nums = [5,7,7,8,8,10]
target = 11
print(obj.searchRange(nums, target))
        