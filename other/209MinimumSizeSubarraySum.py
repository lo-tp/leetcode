from sys import maxint


class Solution(object):
    def minSubArrayLen(self, s, nums):
        size, start, end, res, sum = len(nums), 0, 0, maxint, 0
        while end < size:
            while sum < s and end < size:
                sum += nums[end]
                end += 1
            while start < end and sum >= s:
                res = min(res, end-start)
                sum -= nums[start]
                start += 1
        return res if res!=maxint else 0

