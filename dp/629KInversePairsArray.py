class Solution(object):
    def kInversePairs(self, n, k):
        if not k:
            return 1
        if k >= n:
            return 0
        dp = [[0 for _ in xrange(0, k+1)] for _ in xrange(0, n)]
        dp[0][0] = 1
        for i in xrange(1, n):
            dp[i][0] = 1
            for j in xrange(1, min(i, k)+1):
                for w in xrange(0, min(i-1, j)+1):
                    dp[i][j] += dp[i-1][w]
        return dp[n-1][k] % (10 ** 9+7)
