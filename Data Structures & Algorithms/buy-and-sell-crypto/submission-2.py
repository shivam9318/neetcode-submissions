class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = prices[0]
        for price in prices:
            low = min(price,low)
            profit = price - low
            best = max(best,profit)

        return best