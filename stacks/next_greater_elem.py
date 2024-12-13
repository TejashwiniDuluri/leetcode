

class Solution:

    def nextGreaterElement(self, nums1, nums2):

        result = [-1] * len(nums1)
        di = {value: ind for ind, value in enumerate(nums1)}

        helper_stack = []
        for i in range(len(nums2)):

            # elem in the stack and curr is > than top one so this is the recent top elem
            while helper_stack and nums2[i] > helper_stack[-1]:
                value = helper_stack.pop()
                # find the value from dic and its value is going to be index in result
                ind = di[value]
                result[ind] = nums2[i]

            if nums2[i] in di:
                helper_stack.append(nums2[i])

        return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

nums1 = [1]
nums2 = [1, 2]

nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))
