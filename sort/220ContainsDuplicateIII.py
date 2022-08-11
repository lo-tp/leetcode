from typing import List, Optional
from math import floor


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sz = len(nums)
        seen = {}
        t += 1
        k += 1
        for i in range(0, min(k, sz)):
            j = floor(nums[i] / t)
            if j in seen:
                return True
            elif j + 1 in seen and abs(seen[j + 1] - nums[i]) < t:
                return True
            elif j - 1 in seen and abs(seen[j - 1] - nums[i]) < t:
                return True
            seen[j] = nums[i]
        for i in range(k, sz):
            j = floor(nums[i - k] / t)
            del seen[j]
            j = floor(nums[i] / t)
            if j in seen:
                return True
            elif j + 1 in seen and abs(seen[j + 1] - nums[i]) < t:
                return True
            elif j - 1 in seen and abs(seen[j - 1] - nums[i]) < t:
                return True
            seen[j] = nums[i]
        return False
