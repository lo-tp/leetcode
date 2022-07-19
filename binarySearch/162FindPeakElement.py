from typing import List
from sys import maxsize


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        sz = len(nums)
        def get(index: int):
            if index==-1 or index==sz:
                return -maxsize
            return nums[index]
        l, r = 0, sz - 1
        while l <= r:
            m = l + floor((r - l) / 2)
            if get(m-1)<get(m)>get(m+1):
                return m
            elif get(m-1)>get(m):
                r=m-1
            else:
                l=m+1

