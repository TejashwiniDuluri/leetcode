class Solution:
    def majorityElement(self, nums) -> int:

        count = 0
        ele = nums[0]
        for i in nums:
            
            if i == ele:
                count +=1
            else:
                count -=1
            
            if count == 0:
                ele = i
                count = 1
                
        return ele
    
obj = Solution()
nums = [3,2,3]
print(obj.majorityElement(nums))

        
