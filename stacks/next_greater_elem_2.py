class Solution:
    def nextGreaterElements(self, nums):
        # ===================
        # o(n2)
        # result = []

        # for i in range(len(nums)):
        #     greater_elem = -1
        #     sub_array = nums[i+1:] + nums[:i]
        #     # print(sub_array)
        #     for j in range(len(sub_array)):
        #         # print(sub_array[j], nums[i])
        #         if sub_array[j] > nums[i]:
        #             greater_elem = sub_array[j]
        #             break
        #     # print(greater_elem)
        #     result.append(greater_elem)
        # return result

        # ==========================
        # from start of array
        # stack = []
        # result = {}

        # for num in nums:
        #     while stack and stack[-1] < num:
        #         result[stack.pop()] = num
        #     stack.append(num)

        # # For elements for which next greater element was not found, set it as -1
        # while stack:
        #     result[stack.pop()] = -1

        # return (result.values)

        # ============================
        # from end of array
        # https://www.youtube.com/watch?v=Du881K7Jtk8&ab_channel=takeUforward
        # with out circular check
        # stack = []
        # result = [-1] * len(nums)
        # for i in range(len(nums)-1, -1, -1):
        #     if stack and stack[-1] > nums[i]:
        #         result[i] = stack[-1]
        #         stack.append(nums[i])
        #     elif stack and stack[-1] <= nums[i]:
        #         while stack and stack[-1] <= nums[i]:
        #             stack.pop()
        #         if stack:
        #             result[i] = stack[-1]
        #         else:
        #             result[i] = -1
        #         stack.append(nums[i])
        #     else:
        #         stack.append(nums[i])
        #         result[i] = -1

        # return result
        # =========================================

        # for circular

        stack = []
        nums = nums+nums
        length = len(nums)
        result = [-1] * length

        for i in range(len(nums)-1, -1, -1):
            if stack and stack[-1] > nums[i]:
                result[i] = stack[-1]
                stack.append(nums[i])

            elif stack and stack[-1] <= nums[i]:
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if stack:
                    result[i] = stack[-1]
                else:
                    result[i] = -1
                stack.append(nums[i])

            else:
                stack.append(nums[i])
                result[i] = -1

        return result[0:int(length/2)]


nums = [1, 2, 1]
# nums = [1, 1]
# nums = [1, 2, 3, 4, 3]
nums = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]
obj = Solution()
print(obj.nextGreaterElements(nums))
