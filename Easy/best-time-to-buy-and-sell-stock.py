# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if (diff > max):
                    max = diff
        return max

# Another solution
# Memory: 27.84MB, Beats: 32.45% of users with Python3
class Solution:
    def maxProfit(self, prices):
        min_price, max_diff = prices and prices[0], 0
        for price in prices[1:]:
            max_diff = max(max_diff, price - min_price)
            min_price = min(min_price, price)
        return max_diff
