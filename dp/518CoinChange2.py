from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sz, res = len(coins), 0
        if amount:
            current, stack = 0, [(t, False) for t in range(0, sz)]
            while stack:
                t, flag = stack.pop()
                if flag:
                    if current == amount:
                        res += 1
                    current -= coins[t]
                elif current < amount:
                    current += coins[t]
                    stack.append((t, True))
                    stack.extend([(i, False) for i in range(t, sz)])
        else:
            res = 1
        return res
    def change(self, amount: int, coins: List[int]) -> int:
        dp = tmp = [0]*(amount+1)
        dp[0] = tmp[0] = 1
        for i in range(0, len(coins)):
            for j in range(1, amount+1):
                tmp[j] = dp[j]
                if j-coins[i-1] >= 0:
                    tmp[j] += tmp[j-coins[i-1]]
        dp, tmp = tmp, dp
        return dp[amount]
