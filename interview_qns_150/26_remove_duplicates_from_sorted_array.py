class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        j = 1
        
        while (j < len(nums) -1):

            if nums[i] != nums[j]:
                i+=1
                j+=1
            else:
                while (nums[j] <= nums[i]):
                    j+=1
                
                i+=1
                nums[i] = nums[j]
        return nums
    
obj = Solution()
# nums = [1,1,2]
nums = [0,1,1,1,2,2,3,3,3,4,5]
print(obj.removeDuplicates(nums))



# [0,1] i =0, j =1
# [0,1,1] i =1, j =2
# [0,1,1,1] i =1, j=3
# [0,1,1,1, 2] i =1, j=4

# [0, 1, 2, 1,2] i = 2 , j = 5
# [0 ,1,2,1]