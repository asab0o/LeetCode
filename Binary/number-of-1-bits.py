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