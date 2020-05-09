class Solution(object):
    def minimumTotal(self, T):
        dp, sz = T[-1][:], len(T)
        t = sz-1
        while t:
            tmp = t-1
            for i in xrange(0, t):
                dp[i] = min(dp[i], dp[i+1])+T[tmp][i]
            t -= 1
        return dp[0]

