from typing import List
from math import floor


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(0, n + 1)]
        stack = [(n, i, False) for i in range(2, n + 1)]
        while stack:
            num, divider, flag = stack.pop()
            if num == divider:
                dp[num][divider] = 1
            elif divider == 1:
                dp[num][divider] = num
            elif dp[num][divider] == 0:
                if flag:
                    t = divider - 1
                    dp[num][divider] = max(
                        [k * dp[num - k][t] for k in range(2, num + 2 - divider)]
                    )
                else:
                    stack.append((num, divider, True))
                    t = divider - 1
                    stack.extend(
                        [(num - k, t, False) for k in range(2, num + 2 - divider)]
                    )
        return max(dp[num])
    def integerBreakBetter(self, n: int) -> int:
        if n < 4:
            return n - 1
        elif n == 4:
            return 4
        if n % 3 == 1:
            return 3 ** (floor(n / 3) - 1) * 4
        elif n % 3 == 2:
            return 3 ** floor(n / 3) * 2
        else:
            return 3 ** floor(n / 3)
