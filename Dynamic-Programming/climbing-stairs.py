# first solution
# Time Limit Exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        if n > 2:
            return self.climbStairs(n-2) + 2
        if n == 2:
            return ans + 2
        if n == 1:
            return ans + 1

# Dynamic Programming
# 1. 問題をサブプロブレムに分割する。
# 2. サブプロブレムを解く。
# 3. サブプロブレムの解を保存しておく。
# 4. サブプロブレムの解を組み合わせて、元の問題の解を導く。
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        ans = [0] * (n + 1)
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i - 1] + ans[i - 2]
        return ans[n]

# refactoring
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
