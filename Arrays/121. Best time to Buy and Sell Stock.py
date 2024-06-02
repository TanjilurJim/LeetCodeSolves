class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T.C = O(n)
        # S.C = O(1)
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit =max(max_profit,profit)

        return max_profit
