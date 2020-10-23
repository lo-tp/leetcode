class Solution(object):
    def reverse(self, x):
        is_neg, t, res = x < 0, abs(x), 0
        while t:
            te = t % 10
            res = res*10+te
            t /= 10
        if is_neg:
            res *= -1
        if res < -(1 << 31) or res >= (1 << 31):
            return 0
        return res
