from typing import List
from collections import defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        remaining = defaultdict(lambda: 0)
        for num in nums:
            remaining[num] += 1
        keys = list(remaining.keys())
        keys.sort()
        previous = defaultdict(lambda: 0)
        for key in keys:
            if remaining[key]:
                # appending to existing sequence
                previous[key] += min(previous[key - 1], remaining[key])
                remaining[key] -= min(remaining[key], previous[key - 1])
                if remaining[key]:
                    if key + 2 <= keys[-1]:
                        previous[key + 2] = remaining[key]
                        for k in range(key + 1, key + 3):
                            if remaining[k] >= remaining[key]:
                                remaining[k] -= remaining[key]
                            else:
                                return False
                        remaining[key] = 0
                    else:
                        return False
        return True
