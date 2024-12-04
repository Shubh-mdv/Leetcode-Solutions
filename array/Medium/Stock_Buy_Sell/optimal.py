from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float("inf")
        for i in range(0, n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
obj = Solution()
print(obj.maxProfit(prices))
