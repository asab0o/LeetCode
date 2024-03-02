class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        while (b & mask) > 0:
            
            carry = ( a & b ) << 1 # 繰り上げ
            a = (a ^ b) # 足し算(XOR)
            b = carry # 繰り上げを考慮
        
        # handles overflow
        return (a & mask) if b > 0 else a