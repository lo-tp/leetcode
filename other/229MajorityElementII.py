from typing import List, Optional
from collections import defaultdict
from math import ceil, floor

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        res, sz = [], ceil(len(nums) / 3)
        for num in nums:
            counter[num] += 1
            if counter[num] == sz:
                res.append(num)
        return res

    def majorityElement(self, nums: List[int]) -> List[int]:
        sz = floor(len(nums) / 3)
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif not count1:
                candidate1, count1 = num, 1
            elif not count2:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in [candidate1, candidate2] if nums.count(n) > sz]
