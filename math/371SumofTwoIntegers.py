class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            answer, carry = a ^ b, (a & b) << 1
            a, b = answer, carry
        return a
