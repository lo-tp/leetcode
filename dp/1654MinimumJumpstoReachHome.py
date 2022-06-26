from typing import List
from sys import maxsize


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        tooFar = max(forbidden) + b if a < b else x
        forbidden = set(forbidden)
        dp = [[maxsize, maxsize] for i in range(0, tooFar + 1)]
        dp[0] = [0, 0]
        stack = [(a, 1, True)]
        while stack:
            i, step, flag = stack.pop()
            if i <= 0:
                continue
            j = step + 1
            if i > tooFar:
                if flag:
                    stack.append((i - b, j, False))
                continue
            if not i in forbidden:
                if dp[i][0] > step:
                    dp[i][0] = step
                    stack.append((i + a, j, True))
                if flag and dp[i][1] > step:
                    dp[i][1] = step
                    stack.append((i - b, j, False))
        res = min(dp[x])
        return -1 if res == maxsize else res
