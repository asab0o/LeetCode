# 1のビットの数を数える
# input: n = 00000000000000000000000000001011(32bit)
# output: 3
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            cnt += n & 1
            n >>= 1
        return cnt

# Brian Kernighan's Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n &= (n - 1) # もとの数値の1のバイトを消していく
            count += 1
        return count