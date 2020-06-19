class Solution(object):
    def longestOnes(self, A, K):
        zero_count, res, s = 0, 0, 0
        for e in xrange(0, len(A)):
            if A[e] == 0:
                zero_count += 1
                while zero_count > K:
                    if A[s] == 0:
                        zero_count -= 1
                    s += 1
            res = max(res, e-s+1)
        return res

