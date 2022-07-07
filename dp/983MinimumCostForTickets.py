from typing import List, Optional
from math import floor
from copy import copy
from functools import reduce
from sys import maxsize
from bisect import bisect_left, bisect_right


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        sz = len(days)
        if sz == 1:
            return min(costs)
        days = [day - days[0] + 1 for day in days]
        days.insert(0, 0)
        lastDay = days[-1]
        dp = [maxsize for _ in days]
        dp[0] = 0
        for i in range(1, sz + 1):
            dp[i] = dp[i - 1] + min(costs)
            for j in range(1, i):
                if days[j] + 6 >= days[i]:
                    dp[i] = min(dp[i], dp[j - 1] + costs[1])
                if days[j] + 29 >= days[i]:
                    dp[i] = min(dp[i], dp[j - 1] + costs[2])
        return dp[-1]

    def mincostTicketsBetter(self, days: List[int], costs: List[int]) -> int:
        sz = len(days)
        if sz == 1:
            return min(costs)
        days.append(days[-1] + 31)
        dp = [maxsize for _ in days]
        interval=[1,7,30]
        dp[-1] = 0
        for i in range(sz - 1, -1, -1):
            for j in range(0,3):
                index = bisect_left(days, days[i] + interval[j])
                dp[i] = min(dp[i], dp[index] + costs[j])
        return dp[0]
