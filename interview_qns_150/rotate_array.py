class Solution:

    def reverse(self, nums, start, end):
        
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return nums

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # k = k%len(nums)
        # nums[:] = nums[-k:] + nums[0:-k]
        # return nums
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
print(obj.rotate(nums, k))

      