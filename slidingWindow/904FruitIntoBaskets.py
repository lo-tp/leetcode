from typing import List, Optional
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 1
        t = l = 0
        seen = defaultdict(lambda: 0)
        for r in range(0, len(fruits)):
            curType = fruits[r]
            if not seen[curType]:
                t += 1
            seen[curType] += 1
            while t > 2:
                lType = fruits[l]
                seen[lType] -= 1
                if not seen[lType]:
                    t -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
