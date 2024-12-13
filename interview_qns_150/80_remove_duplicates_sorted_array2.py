class Solution:
    def removeDuplicates(self, nums) -> int:
        # i = 0
        # j = 1
        # k = 1

        # while (j < len(nums)-1):
        #     if nums[i] != nums[j]:                 
        #         k = 1

        #     else:                
        #         k+=1
                
        #     if k<=2: 
        #         nums[k] = nums[j]
        #         k+=1

        #     i+=1
        #     j+=1

        # return nums
        if not nums:
            return 0
    
        write_index = 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index



nums = [1,1,1,2,2,3]
# nums = [1,2,3,1,2]





obj = Solution()
print(obj.removeDuplicates(nums))
        