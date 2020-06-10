class Solution(object):
    def minDistance(self, word1, word2):
        sz1, sz2 = len(word1), len(word2)
        dp = [[0 for _ in xrange(0, sz2+1)] for _ in xrange(0, sz1+1)]
        for i in xrange(1, sz1+1):
            for j in xrange(1, sz2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return sz1+sz2-2*dp[sz1][sz2]
