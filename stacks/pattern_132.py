class Solution:
    def find132pattern(self, nums) -> bool:
        # side by side solution
        # i = 0
        # j = 1
        # k = 2
        # nums_length = len(nums)
        # if nums_length < k:
        #     return False
        # while k < nums_length:
        #     if nums[i] < nums[k] < nums[j]:
        #         return True
        #     i += 1
        #     j += 1
        #     k += 1
        # return False

        # ===========================
        stack = []
        minimum = nums[0]

        for i in nums[1:]:
            print(minimum, stack)
            while stack and stack[-1][1] <= i:
                stack.pop()

            if stack and stack[-1][0] < i < stack[-1][1]:
                return True

            stack.append([minimum, i])
            minimum = min(minimum, i)

        return False


nums = [1, 2, 3, 4]
# nums = [3, 1, 4, 2]
# nums = [-1, 3, 2, 0]
# nums = [3, 5, 0, 3, 4]
# nums = [-2, 1, 2, -2, 1, 2]
# nums = [1, 0, 1, -4, -3]
obj = Solution()
print(obj.find132pattern(nums))
