class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = [2**i for i in xrange(0, 32)]
        res = 0
        for i in xrange(0, 32):
            if n & bits[i]:
                res ^= bits[31-i]
        if res & bits[-1]:
            return -(2**32-res)
        return res
