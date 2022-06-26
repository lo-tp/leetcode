from typing import List
from functools import reduce


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp = {}
        dp[0] = True
        allOptions = [i for i in range(1, maxChoosableInteger + 1)]

        def dpFunc(options: List[int], total: int):
            key = tuple(options)
            if options[-1] >= total:
                dp[key] = True
            summation = sum(options)
            if summation == total:
                dp[key] = True if len(options) % 2 else False
            elif summation < total:
                dp[key] = False
            elif key not in dp:
                dp[key] = False
                for index in range(0, len(options)):
                    nextOptions, nextTotal = (
                        options[:index] + options[index + 1 :],
                        total - options[index],
                    )
                    if not dpFunc(nextOptions, nextTotal):
                        dp[key] = True
                        break
            return dp[key]

        return dpFunc(allOptions, desiredTotal)

