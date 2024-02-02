# I solved the problem myself.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        left, right = 0, len(height)-1
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            amount = width * min_height
            max_amount = max(max_amount, amount)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_amount
