from collections import defaultdict

class Solution(object):
    def maxUncrossedLines(self, A, B):
        sz_a, sz_b = len(A)+1, len(B)+1
        dp = [[0 for i in xrange(0, sz_a)] for j in xrange(0, sz_b)]
        for i in xrange(1, sz_a):
            for j in xrange(1, sz_b):
                t, te = j-1, i-1
                dp[j][i] = max(dp[t][i], dp[j][te], dp[t][te] +
                               (1 if A[te] == B[t] else 0))
        return dp[-1][-1]
