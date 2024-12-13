class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        # circular_nums = nums+nums
        # nums_len = len(nums)
        
        # curr_sum = 0
        # max_sum = nums[0]
        
        # for i in range(0, nums_len):
            
        #     j = 0
            
        #     while j < nums_len:
            
        #         curr_sum = curr_sum + circular_nums[i+j]
        #         if max_sum < curr_sum:
        #             max_sum = curr_sum
        #         j+=1  
        #     curr_sum = 0 
        # return max_sum 
        
        ###### above is reaching time limit ######
        
        # total_sum = 0
        
        # max_sum = nums[0]
        # curr_max = 0
        
        # min_sum = nums[0]
        # current_min = 0
        
        # for i in nums:
        #     total_sum+=i
            
        #     current_min = min (i, current_min+i)
        #     min_sum = min (min_sum, current_min)
            
        #     curr_max = max(i, curr_max+i)
        #     max_sum = max(max_sum, curr_max)
        
        # if max_sum < 0:
        #     return max_sum
        
        
        # return max (max_sum, total_sum - min_sum)  
        
        ##### just optimizing above for speed of execution #####  
        
        total_sum = 0
        
        max_sum = nums[0]
        curr_max = 0
        
        min_sum = nums[0]
        current_min = 0
        
        for i in nums:
            total_sum+=i
            
            current_min = i if i < current_min+i else current_min+i 
            min_sum = min_sum if min_sum< current_min else current_min
            
            curr_max = i if i> curr_max+i else curr_max+i
            max_sum = max_sum if max_sum > curr_max else curr_max
        
        if max_sum < 0:
            return max_sum
        
        
        return max_sum if max_sum > total_sum - min_sum else total_sum - min_sum
            
        
            
        
        
        
        

nums = [1,-2,3,-2]
# nums = [5, -3, 5]
# nums = [-3,-2,-3]
obj = Solution()
print(obj.maxSubarraySumCircular(nums))