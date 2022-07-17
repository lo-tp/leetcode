from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        s = [(-aliceValues[i] - bobValues[i], i) for i in range(0, len(aliceValues))]
        s.sort()
        aPoint = bPoint = 0
        for i in range(0, len(aliceValues)):
            if i % 2:
                bPoint += bobValues[s[i][1]]
            else:
                aPoint += aliceValues[s[i][1]]
        t = aPoint - bPoint
        if t > 0:
            return 1
        elif t < 0:
            return -1
        return 0
