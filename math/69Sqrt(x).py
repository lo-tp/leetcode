class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 0, x // 2
        while l < r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m
            else:
                l = m + 1
        return l - 1 if l*l>x else l
