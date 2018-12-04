class Solution(object):
    def numTrees(self, n):
        sz = n+1
        dp = [0]*sz
        if sz > 1:
            dp[0], dp[1] = 1, 1
            for i in xrange(2, sz):
                for k in xrange(1, i+1):
                    dp[i] += (dp[k-1]*dp[i-k])
        return dp[n]
