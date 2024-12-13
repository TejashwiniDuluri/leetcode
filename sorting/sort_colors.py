class Solution:
    def sortColors(self, nums):
        low, curr, high = 0, 0, len(nums)-1

        while curr <= high:
            if nums[curr] == 2:

                # swap current and high
                temp = nums[high]
                nums[high] = nums[curr]
                nums[curr] = temp

                high -= 1

            elif nums[curr] == 1:
                curr += 1

            else:  # 0 case
                temp = nums[curr]
                nums[curr] = nums[low]
                nums[low] = temp
                low += 1
                curr += 1

        return nums


nums = [2, 0, 2, 1, 1, 0]
nums = [2, 0, 1]
obj = Solution()
print(obj.sortColors(nums))
