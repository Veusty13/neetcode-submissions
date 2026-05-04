class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0 
        r = 1
        max_profit = 0
        while r < n :
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if profit > 0 :
                r += 1
            else :
                l += 1
                r = l + 1
        return max_profit