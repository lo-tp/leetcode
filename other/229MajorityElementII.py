from typing import List, Optional
from collections import defaultdict
from math import ceil

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        res, sz = [], ceil(len(nums) / 3)
        for num in nums:
            counter[num] += 1
            if counter[num] == sz:
                res.append(num)
        return num
