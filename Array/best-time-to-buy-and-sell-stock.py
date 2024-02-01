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

# use float method for init
class Solution:
    def maxProfit(self, prices):
        min_price = float("inf")
        max_profit = 0

        for num in prices:
            min_price = min(min_price, num)
            max_profit = max(max_profit, num - min_price)
        
        return max_profit

# right と left のポインタを使用
class Solution:
    def maxProfit(self,prices):
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            print(left, right)
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit =max(current_profit, max_profit)
            else:
                # 最小値はprices[right]ではないことがわかったため
                left = right
            right += 1
        return max_profit