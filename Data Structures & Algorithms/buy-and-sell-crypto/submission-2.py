class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)
        if n == 0:
            return 0
        if len(set(prices)) == 1:
            return 0
        l = 0
        r = 1
        max_profit: int = 0
        while r <= n - 1:
            current_profit: int = prices[r] - prices[l]
            if current_profit > 0:
                max_profit = max(max_profit, current_profit)
            else:
                l = r
            r += 1
        return max_profit


