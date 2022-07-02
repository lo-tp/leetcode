from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlicesTLE(self, nums: List[int]) -> int:
        res = 0
        dp = []
        for i in range(1, len(nums)):
            tmp = []
            for prev, nextElement, prevSeq in dp:
                if nums[i] == nextElement:
                    res += 1
                    tmp.append((nums[i], 2 * nums[i] - prev, prevSeq+[i]))
                tmp.append((prev, nextElement, prevSeq))
            # print(tmp)
            tmp, dp = dp, tmp
        return res

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        sz = len(nums)
        dp = [defaultdict(lambda: 0) for _ in nums]
        for i in range(1, sz):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                t = 0
                if diff in dp[j]:
                    t += dp[j][diff]
                dp[i][diff] += t + 1
                res += t
        return res
