class Solution:
    def canJump(self, nums) -> bool:
        
        if len(nums) == 1:
            return 0
        
        destination = len(nums)-1
        curr_max_reach = 0
        max_reach = 0   
        max_steps = 0     

        for index, i in enumerate(nums):   
            curr_max_reach = max(i + index, curr_max_reach)
                        
            if (index == max_reach):
                max_steps+=1
                max_reach = curr_max_reach
                
                if curr_max_reach >= destination:
                    return max_steps

        return max_steps
            
        

nums = [2, 3, 1, 1, 4]
# nums = [2,3,0,1,4]
# nums = [0]
# nums = [1,2,1,1,1]
nums = [1,1,1,1]
nums = [1,1,1,1,1]
obj = Solution()
print(obj.canJump(nums))


