class Solution:

    def maxA(self, N):
        dp = [0]*(N+1)
        for i in range(1, min(N+1, 4)):
            dp[i] = i
        for i in range(4, N+1):
            dp[i] = dp[i-1]+1
            for j in range(3, i):
                dp[i] = max(dp[i], dp[j-2]*(i-j+1))
        return dp[N]
