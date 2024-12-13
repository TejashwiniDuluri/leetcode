class Solution:
    def finalPrices(self, prices):
        stack = []
        result = []
        for i in prices[::-1]:
            if stack:
                if stack[-1] < i:
                    result.insert(0, i - stack[-1])
                else:
                    while (stack and stack[-1] > i):
                        stack.pop()
                    if stack:
                        result.insert(0, i - stack[-1])
                    else:
                        result.insert(0, i)

                stack.append(i)
            else:
                result.insert(0, i)
                stack.append(i)
        return result


obj = Solution()
prices = [8, 4, 6, 2, 3]
prices = [1, 2, 3, 4, 5]
prices = [10, 1, 1, 6]
prices = [10, 9, 8, 7, 6]
print(obj.finalPrices(prices))
