from typing import List
from math import floor
from functools import cache


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz == 1 or nums[0] > nums[1]:
            return nums[0]
        l, r = 0, sz - 1
        while l <= r:
            m = l + floor((r - l) / 2)
            if not m or m == sz - 1:
                return m
            elif nums[m - 1] > nums[m]:
                r = m - 1
            elif nums[m + 1] > m:
                l = m + 1
            else:
                return m

