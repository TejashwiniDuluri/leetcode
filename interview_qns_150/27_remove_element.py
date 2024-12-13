class Solution:
    def removeElement(self, nums, val: int) -> int:
        
        # k = -1
        # count=0

        # for i in range(len(nums)-1, -1, -1):            
        #     print(i)
        #     if nums[i] == val and nums[k] == val:
        #         nums[k] = "_"
        #         k-=1                
            
        #     elif nums[i] == val and nums[k] != val:
        #         nums[i] = nums[k]
        #         nums[k] = "_"                
        #         k=-1
            
                
        
        #     print(nums)
        # return len(nums)-count
        k = 0
        for i in range(len(nums)):
            
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        
        # for i in range(k, len(nums)):
        #     nums[i] = "_"
        return nums






nums = [3,2,2,3,4]
val = 3
obj = Solution()
print(obj.removeElement(nums, val))

        
