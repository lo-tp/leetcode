class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        sz1, sz2, res = len(str1), len(str2), ''
        dp = [['' for _ in xrange(0, sz2+1)] for _ in xrange(0, sz1+1)]
        for i in xrange(0, sz1):
            for j in xrange(0, sz2):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = '{}{}'.format(dp[i][j], str1[i])
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
        i, j = 0, 0
        for c in dp[-1][-1]:
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return '{}{}{}'.format(res, str1[i:], str2[j:])
