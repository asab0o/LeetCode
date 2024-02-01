# Inputの配列に対して, i番目の数を除いたすべての積を配列に格納(Output)
# RuntimeはO(n), division operationは使用しない

# Runs in O(n^2)...
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            newList = nums[:]
            newList.remove(nums[i])
            x = 1
            for value in newList:
                x *= value
            results.append(x)
        return results

# Runs in O(n)!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before_multi = 1
        after_multi = 1
        results = [0]*n
        for i in range(n):
            # results[0] = 1
            # results[1] = 1 * nums[0]
            # ...
            # results[n] = 1 * nums[0] ... * nums[n-1]
            results[i] = before_multi
            before_multi *= nums[i]
        for i in range(n-1, -1, -1):
            # results[n] = (1 * nums[0] ... * nums[n-1]) * 1
            # ...
            # results[1] = (1 * nums[0]) * (1 * nums[n-1] ... * nums[2])
            # results[0] = 1 * (1 * nums[n-1] ... * nums[1])
            results[i] *= after_multi
            after_multi *= nums[i]
        return results