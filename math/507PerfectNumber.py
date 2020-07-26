from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num):
        if num < 0:
            return False
        t = 1
        te = int(sqrt(num))
        for i in xrange(2, te):
            if not num % i:
                t += i
                t += num/i
        if not num % te:
            t += te
            m = num/te
            if m != te:
                t += m
        return t == num
