from typing import List, Optional
from collections import defaultdict
from math import ceil, floor

def findMajorityElement(nums: List[int], sz: int) -> List[int]:
    sz = 2
    counts = [0] * sz
    data = [0] * sz
    for num in nums:
        flag = True
        for i in range(0, sz):
            if data[i] == num:
                counts[i] += 1
                flag = False
                break
        if flag:
            for i in range(0, sz):
                if not counts[i]:
                    data[i] = num
                    counts[i] = 1
                    flag = False
                    break
        if flag:
            counts = [c - 1 for c in counts]
    minCount = floor(len(nums) / (sz + 1))
    return [
        data[i] for i in range(0, sz) if counts[i] and nums.count(data[i]) > minCount
    ]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return findMajorityElement(nums, 2)

