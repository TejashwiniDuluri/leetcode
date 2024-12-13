class Solution:
    def maxSlidingWindow(self, nums, k):

        dequeue = []
        result = []
        length = 0

        for i in range(len(nums[0:k])):
            while dequeue and dequeue[-1][1] < nums[i]:
                dequeue.pop()
                length -= 1
            dequeue.append((i, nums[i]))
            length += 1

        result.append(dequeue[0][1])

        for i in range(k, len(nums)):
            while dequeue and dequeue[0][0] <= i-k:
                dequeue.pop(0)
                length -= 1

            while (dequeue and dequeue[-1][1] < nums[i]):
                length -= 1
                dequeue.pop()

            dequeue.append((i, nums[i]))
            length += 1

            result.append(dequeue[0][1])

        ########### above is normal sol############
        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
nums = [1]
k = 1
nums = [1, -1]
k = 1
nums = [5, 3, 4]
k = 1
nums = [7, 2, 4]
k = 2

obj = Solution()
print(obj.maxSlidingWindow(nums, k))
