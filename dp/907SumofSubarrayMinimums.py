from typing import List
from sys import maxsize


class Solution:
    def sumSubarrayMinsTLE(self, arr: List[int]) -> int:
        dp = [maxsize]
        res = 0
        for i in arr:
            tmp = [maxsize]
            for j in dp:
                tmp.append(min(i, j))
            dp = tmp
            res += (sum(dp) - maxsize) % (10**9 + 7)
        return res % (10**9 + 7)

    def sumSubarrayMins(self, arr: List[int]) -> int:
        dp = [arr[0]]
        monoStack = [(arr[0], 0)]
        for i in range(1, len(arr)):
            while monoStack and monoStack[-1][0] > arr[i]:
                monoStack.pop()
            dp.append(
                dp[monoStack[-1][1]] + arr[i] * (i - monoStack[-1][1])
                if monoStack
                else (i + 1) * arr[i]
            )
            monoStack.append((arr[i],i))
        return sum(dp) % (10**9 + 7)
