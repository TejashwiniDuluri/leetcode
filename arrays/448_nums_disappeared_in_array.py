
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        missing = []
        dict = {}
        
        for i in nums:
            dict[i] = i

        for i in range(1, length+1):
            if i not in dict:
                missing.append(i)
        
        return missing

        
        

nums = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))