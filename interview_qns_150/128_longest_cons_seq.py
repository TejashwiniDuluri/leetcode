from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if nums == []:
        #     return 0
        
        # nums = sorted(set(nums))
        # count = 1
        # max_count = 1

        # for i in range(0, len(nums)-1):  
        #     if nums[i+1] - nums[i] == 1:
        #         count+=1
        #     else:
        #         count = 1
        #     max_count = max(count, max_count)
        # return max_count

        # ==== usign hashmap =====
        if nums == []:
            return 0
        hash_map = {}
        for i in nums:
            hash_map[i] = i
        
        max_count = 1

        for val in nums:
            count = 1
            cur_val = val
            if cur_val - 1 in hash_map: # this means it is already processed so dont run
                continue
            while cur_val + 1 in hash_map:
                count +=1
                cur_val+=1
                
            max_count = max(count, max_count)
        return max_count


obj = Solution()
nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums =[9,1,4,7,3,-1,0,5,8,-1,6]
# nums =[1,2,0,1] #=> [0, 1,1,2]
print(obj.longestConsecutive(nums))