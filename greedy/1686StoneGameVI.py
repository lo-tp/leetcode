from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        t = sorted(
            [
                (-aliceValues[i] - bobValues[i], aliceValues[i], bobValues[i])
                for i in range(0, len(aliceValues))
            ]
        )
        res = reduce(
            lambda accu, i: accu - (t[i][2] if i % 2 else -t[i][1]), range(0, len(t)), 0
        )
        if res < 0:
            return -1
        elif res > 0:
            return 1
        return res

