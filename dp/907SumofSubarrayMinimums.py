from typing import List
from sys import maxsize


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        dp = [maxsize]
        res = 0
        for i in arr:
            tmp = [maxsize]
            for j in dp:
                tmp.append(min(i, j))
            dp = tmp
            res += (sum(dp) - maxsize) % (10**9 + 7)
        return res % (10**9 + 7)
