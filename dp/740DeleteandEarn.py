from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        u, d = list(set(nums)), Counter(nums)
        u.sort()
        sz = len(u)
        if sz == 1:
            return sum(nums)
        dp = [0] * (sz + 1)
        dp[sz - 1] = u[-1] * d[u[-1]]
        for i in range(sz - 2, -1, -1):
            dp[i] = u[i] * d[u[i]] + (dp[i + 1] if u[i] + 1 != u[i + 1] else dp[i + 2])
        return max(dp[0], dp[1])
