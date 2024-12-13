from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        nums_len = len(nums)
        
        triplets = set()
        for i in range(nums_len-2):
            j = i+1
            k = nums_len-1
            while (i < j< k):
                val = nums[i] + nums[j] + nums[k]
                if val== 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif val > 0:
                    k-=1
                elif val < 0:
                    j+=1
                
        return list(triplets)




        
        

nums = [-1,0,1,2,-1,-4]
Output = [[-1,-1,2],[-1,0,1]]
obj = Solution()
print(obj.threeSum(nums))