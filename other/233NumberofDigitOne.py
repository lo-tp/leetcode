class Solution(object):
    def countDigitOne(self, n):
        res = 0
        for i in xrange(1, n+1):
            while i:
                if i % 10 == 1:
                    res += 1
                i /= 10
        return res

