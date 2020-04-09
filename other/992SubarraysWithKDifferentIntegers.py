from collections import defaultdict


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        sz = len(A)
        data = [0, 0]
        for i, j in enumerate([K-1, K]):
            t, te, l = defaultdict(lambda: 0), 0, 0
            for r in xrange(0, sz):
                if not t[A[r]]:
                    te += 1
                t[A[r]] += 1
                if te > j:
                    while t[A[l]] > 1:
                        t[A[l]] -= 1
                        l += 1
                    t[A[l]] -= 1
                    l += 1
                    te -= 1
                data[i] += (r-l+1)
        return data[1]-data[0]

