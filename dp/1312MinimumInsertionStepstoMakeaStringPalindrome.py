class Solution(object):
    def minInsersions(self, s):
        sz, reversed = len(s), s[::-1]
        dp, tmp = [0]*(sz+1), [0]*(sz+1)
        for i in range(0, sz):
            for j in range(0, sz):
                if s[i] == reversed[j]:
                    tmp[j+1] = dp[j]+1
                else:
                    tmp[j+1] = max(dp[j+1], tmp[j])
            dp, tmp = tmp, dp
        return sz-dp[-1]
    def minInsertionsBetter(self, s: str) -> int:
        sz = len(s)
        dp, tmp = [0] * sz, [0] * sz
        for i in range(sz - 1, -1, -1):
            tmp[i] = 1
            for j in range(i + 1, sz):
                if s[i] == s[j]:
                    tmp[j] = dp[j - 1] + 2
                else:
                    tmp[j] = max(dp[j], tmp[j - 1])
            dp, tmp = tmp, dp
        return sz - dp[-1]
