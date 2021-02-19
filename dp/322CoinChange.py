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
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        stack = [(amount, False)]
        while stack:
            t, flag = stack.pop()
            if dp[t] == -1:
                if not flag:
                    stack.append((t, True))
                    stack.extend([(t-c, False)
                                  for c in coins if t >= c and dp[t-c] == -1])
                else:
                    tmp = [dp[t-c]
                           for c in coins if t >= c and dp[t-c] != None]
                    dp[t] = min(tmp)+1 if tmp else None
        return dp[amount] if dp[amount] != None else -1
