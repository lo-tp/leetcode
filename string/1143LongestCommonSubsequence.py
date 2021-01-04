class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        sz1, sz2 = len(text1), len(text2)
        data = [['' for _ in xrange(0, sz2+1)] for _ in xrange(0, sz1+1)]
        for i in xrange(1, sz1+1):
            for j in xrange(1, sz2+1):
                if text1[i-1] == text2[j-1]:
                    data[i][j] = data[i-1][j-1]+text1[i-1]
                else:
                    data[i][j] = max(data[i][j-1], data[i-1][j], key=len)
        return len(data[-1][-1])

    def longestCommonSubsequence(self, text1, text2):
        sz1, sz2 = len(text1), len(text2)
        tmp, dp = [0]*(sz2+1), [0]*(sz2+1)
        for i in range(0, sz1):
            for j in range(0,  sz2):
                tmp[j] = dp[j] + \
                    1 if text1[i] == text2[j] else max(tmp[j], dp[j+1])
            dp = tmp
        return dp[-1]
