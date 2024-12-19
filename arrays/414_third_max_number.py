class Solution:
    def thirdMax(self, nums) -> int:
        # nums = sorted(list(set(nums)), reverse=True)

        # return nums[0] if len(nums) < 3 else nums[2]
        
        # other approach 

        first = second = third = None

        for i in nums:
            
            if first == i or second == i or third == i:
                continue

            if first is None or i > first:
                third = second
                second = first
                first = i
            
            elif second is None or i > second:
                third = second
                second = i
            
            elif third is None or i > third:
                third = i
            
            return third if third is not None else first
    

            
        
        

nums = [2,2,3,1]
obj = Solution()
print(obj.thirdMax(nums))