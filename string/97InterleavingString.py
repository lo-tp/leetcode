from collections import Counter


def lcs(s1, s2):
    sz1, sz2 = len(s1), len(s2)
    dp = [['' for _ in range(0, sz2+1)]for _ in range(0, sz1+1)]
    for i in range(0, sz1):
        for j in range(0, sz2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]+s1[i]
            elif len(dp[i][j+1]) > len(dp[i+1][j]):
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = dp[i+1][j]
    return dp[-1][-1]


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        sz1, sz2, sz3 = len(s1), len(s2), len(s3)
        return len(lcs(s1, s3)) == sz1 and len(lcs(s2, s3)) == sz2 and (Counter(s1) + Counter(s2)) == Counter(s3)
