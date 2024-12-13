class Solution:
    def canJump(self, nums) -> bool:

        max_reach = len(nums)-1
        cu_step = 0
        
        for index, i in enumerate(nums):
            if cu_step < index:
                return False
            
            cu_step = max(cu_step, index + i)
            
            if cu_step >= max_reach:
                return True
            
        return False



nums = [2, 3, 1, 1, 4]
# nums = [3,2,1,0,4]
obj = Solution()
print(obj.canJump(nums))