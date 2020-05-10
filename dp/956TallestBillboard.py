from collections import defaultdict
from copy import copy


class Solution(object):
    def tallestBillboard(self, rods):
        dp = defaultdict(lambda: 0)
        dp[0] = 0
        for i in rods:
            for key, val in dp.items():
                dp[key+i] = max(dp[key+i], val)
                t = abs(key-i)
                dp[t] = max(dp[t], val+min(key, i))
        return dp[0]

