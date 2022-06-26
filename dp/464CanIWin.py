from typing import List
from sys import maxsize

from functools import reduce


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp = {}
        allOptions = [i for i in range(1, maxChoosableInteger + 1)]
        stack = [(allOptions, desiredTotal, 0, tuple(allOptions))]
        count=100
        while stack and count:
            options, total, index, key = stack.pop()
            if options[-1] >= total:
                dp[key] = True
            elif sum(options) == total:
                dp[key] = True if len(options) % 2 else False
            elif sum(options) < total:
                dp[key] = False
            else:
                nextOptions, nextTotal = (
                    options[:index] + options[index + 1 :],
                    total - options[index],
                )
                nextKey = tuple(nextOptions)
                if nextKey in dp:
                    if not dp[nextKey]:
                        dp[key] = True
                    elif index < len(options) - 1:
                        stack.append((options, total, index + 1, key))
                    else:
                        dp[key] = False
                else:
                    stack.append((options, total, index, key))
                    stack.append((nextOptions, nextTotal, 0, nextKey))
            count-=1
        return dp[tuple(allOptions)]
