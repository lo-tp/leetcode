class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 11
        t, res = 9, 10
        for i in range(2, n+1):
            t = t*(10-i-1)
            res += t
        return res
