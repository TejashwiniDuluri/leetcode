class Solution:
    def maxProfit(self, prices) -> int:

        curr_buy = prices[0]
        max_profit = 0

        for i in prices:
            if i > curr_buy:
                curr_profit = i - curr_buy
                max_profit = max(max_profit, curr_profit)
            if i < curr_buy:
                curr_buy = i
        return max_profit



obj = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(obj.maxProfit(prices))



        
        

