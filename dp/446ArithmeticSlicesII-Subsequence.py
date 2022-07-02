from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
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
            for j in range(0, i):
                tmp.append((nums[i], 2 * nums[i] - nums[j],[j,i]))
            tmp, dp = dp, tmp
        return res
