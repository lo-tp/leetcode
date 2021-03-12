from typing import List
from sys import maxsize


class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        sz = len(m)
        dp, tmp = [maxsize]*(sz+2), [maxsize]*(sz+2)
        for i in range(0, sz):
            dp[i+1] = m[-1][i]

        for i in range(sz-2, -1, -1):
            for j in range(1, sz+1):
                tmp[j] = m[i][j-1]+min(dp[j-1], dp[j+1], dp[j])
            dp = tmp
        return min(dp)

    def minFallingPathSum(self, m: List[List[int]]) -> int:
        sz = len(m)
        dp, tmp = [maxsize]*(sz+2), [maxsize]*(sz+2)
        for i in range(0, sz):
            dp[i+1] = m[-1][i]

        for i in range(sz-2, -1, -1):
            for j in range(1, sz+1):
                tmp[j] = m[i][j-1]+min(dp[j-1], dp[j+1], dp[j])
            tmp, dp = dp, tmp
        return min(dp)
