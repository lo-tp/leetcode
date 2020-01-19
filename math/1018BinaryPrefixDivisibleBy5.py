class Solution(object):
    def prefixesDivBy5(self, A):
        sz, t, res = len(A), 0, [False for i in A]
        for i in xrange(0, sz):
            t *= 2
            if A[i]:
                t += 1
            t %= 5
            if not t:
                res[i] = True
        return res

