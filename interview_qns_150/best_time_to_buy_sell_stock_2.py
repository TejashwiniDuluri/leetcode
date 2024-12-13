class Solution:
    def maxProfit(self, prices) -> int:

        max_profit = 0
        curr_buy = prices[0]

        for i in prices:
            
            if i > curr_buy:
                curr_profit = i - curr_buy
                max_profit += curr_profit
                curr_buy = i

            if i < curr_buy:
                curr_buy = i

        return max_profit



obj = Solution()
prices = [7,1,5,3,6,4]
print(obj.maxProfit(prices))
        