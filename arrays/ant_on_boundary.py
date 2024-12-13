class Solution:
    def returnToBoundaryCount(self, nums) -> int:

        boundary = 0
        visited = 0
        for i in nums:
            boundary += i
            if boundary == 0:
                visited += 1
        return visited


nums = [2, 3, -5]
nums = [3, 2, -3, -4]
nums = [-9, 9, 6, -6]
obj = Solution()
print(obj.returnToBoundaryCount(nums))
