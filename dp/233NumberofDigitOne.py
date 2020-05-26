from math import log10

class Solution(object):
    def countDigitOneTLE(self, n):
        res = 0
        for i in xrange(1, n+1):
            while i:
                if i % 10 == 1:
                    res += 1
                i /= 10
        return res

    def countDigitOne(self, n):
        if n <= 0:
            return 0
        ord_0, res, t = ord('0'), 0, [1]
        for i in xrange(1, int(log10(n))):
            t.append(t[-1]*10+10**i)
        while n:
            te, tem = list(str(n)), int(log10(n))-1
            tmp, te[0] = ord(te[0])-ord_0, '0'
            n = int(''.join(te))
            if tem >= 0:
                res += tmp*t[tem]
                res += n+1 if tmp == 1 else 10**(tem+1)
            else:
                res += 1
        return res

    def countDigitOne(self, n):
        if n <= 0:
            return 0
        ord_0, res, t = ord('0'), 0, [
            (i+1)*10**i for i in xrange(0, int(log10(n)))]
        while n:
            te, tem = list(str(n)), int(log10(n))-1
            tmp, te[0] = ord(te[0])-ord_0, '0'
            n = int(''.join(te))
            if tem >= 0:
                res += tmp*t[tem]
                res += n+1 if tmp == 1 else 10**(tem+1)
            else:
                res += 1
        return res
