class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profit_list = []
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i,len(prices)):
                profit = prices[j] - prices[i]
                profit_list.append(profit)
                max_profit = max(profit_list)
        return max(profit_list)