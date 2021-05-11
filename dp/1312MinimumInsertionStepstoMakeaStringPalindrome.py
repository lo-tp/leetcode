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
