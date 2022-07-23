from typing import List, Optional
from math import floor


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        sz1, sz2 = len(nums1), len(nums2)
        tmp, dp = [0] * (sz2 + 1), [0] * (sz2 + 1)
        res = 0
        for i in range(0, sz1):
            for j in range(0, sz2):
                if nums1[i] == nums2[j]:
                    tmp[j + 1] = dp[j] + 1
                else:
                    tmp[j + 1] = 0
            tmp, dp = dp, tmp
            res = max(res, max(dp))
        return res
