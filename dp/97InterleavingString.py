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
    def isInterleaveWA(self, s1, s2, s3):
        sz1, sz2, sz3 = len(s1), len(s2), len(s3)
        return len(lcs(s1, s3)) == sz1 and len(lcs(s2, s3)) == sz2 and (Counter(s1) + Counter(s2)) == Counter(s3)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sz1, sz2, sz3 = len(s1), len(s2), len(s3)
        if sz1 + sz2 == sz3:
            dp, tmp = [False] * (sz2 + 1), [False] * (sz2 + 1)
            dp[0] = True
            for i in range(0, sz1 + 1):
                t = i
                for j in range(0, sz2 + 1):
                    if not i and not j:
                        tmp[0] = True
                    elif not i:
                        tmp[j] = tmp[j - 1] and s2[j - 1] == s3[t - 1]
                    elif not j:
                        tmp[j] = dp[j] and s1[i - 1] == s3[t - 1]
                    else:
                        tmp[j] = (dp[j] and s1[i - 1] == s3[t - 1]) or (
                            tmp[j - 1] and s2[j - 1] == s3[t - 1]
                        )
                    t += 1
                tmp, dp = dp, tmp
            return dp[-1]
        return False

