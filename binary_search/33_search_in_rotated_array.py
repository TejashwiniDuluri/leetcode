from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        low = 0
        high = nums_len-1

        while low <= high:
            mid = (low + high) //2
            
            if nums[mid] == target:
                return mid
                        
            if nums[mid] > nums[high]:
                if target < high:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        if nums [mid] == target:
            return mid
        else:
            return -1


obj = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
print(obj.search(nums, target))
