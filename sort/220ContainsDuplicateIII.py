from typing import List, Optional
from math import floor


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        index = {}
        t += 1
        for i in range(0, len(nums)):
            tmp = floor(nums[i] / t)
            if tmp in index and i - index[tmp] <= k:
                return True
            index[tmp] = i
            tmp -= 1
            if (
                tmp in index
                and i - index[tmp] <= k
                and abs(nums[i] - nums[index[tmp]]) < t
            ):
                return True
            tmp += 2
            if (
                tmp in index
                and i - index[tmp] <= k
                and abs(nums[i] - nums[index[tmp]]) < t
            ):
                return True
        return False
