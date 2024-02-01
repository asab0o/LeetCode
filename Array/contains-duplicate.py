# My first solution
# Code [TLE]:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 二重ループの計算量がO(n^2)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                print(i, j)
                if nums[i] == nums[j]:
                    return True
        else:
            return False

# using the hash set data structure
# The time complexity is O(n).
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# sorting
# The time complexity is O(n log n).
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
