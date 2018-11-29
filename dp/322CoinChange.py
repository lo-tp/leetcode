class Solution(object):
    def coinChange(self, coins, amount):
        dp = {0: 0}
        for i in xrange(1, amount+1):
            for k in coins:
                if i-k in dp:
                    if i in dp:
                        dp[i] = min(dp[i], dp[i-k]+1)
                    else:
                        dp[i] = dp[i-k]+1
        return dp[amount] if amount in dp else -1
