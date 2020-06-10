class Solution(object):
    def longestPalindromeSubseq(self, s):
        t, sz = s[::-1], len(s)
        dp = [[0 for _ in xrange(0, sz+1)] for _ in xrange(0, sz+1)]
        for i in xrange(1, sz+1):
            for j in xrange(1, sz+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[sz][sz]
