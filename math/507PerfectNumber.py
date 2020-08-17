from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 0:
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

    def checkPerfectNumber(self, num):
        res, non_prime = set(), set()
        for i in xrange(2, 16384):
            if i not in non_prime:
                t = i*2
                while t < 16384:
                    non_prime.add(t)
                    t *= 2
        for i in xrange(1, 14):
            t = 2**i
            te = t*2-1
            if te not in non_prime:
                res.add(t*te)
        return num in res
