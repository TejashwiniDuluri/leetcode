class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:

        max_count = 0
        curr_count = 0

        for i in nums:

            if i == 1:
                curr_count += 1
                max_count = max_count if max_count > curr_count else curr_count
            else:
                curr_count = 0
        
        return max_count
        

nums = [1,1,0,1,1,1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))