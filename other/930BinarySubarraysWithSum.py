from typing import List, Optional
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(lambda: 0)
        seen[0] = 1
        res = 0
        t = 0
        for num in nums:
            t += num
            res += seen[t - goal]
            seen[t] += 1
        return res
