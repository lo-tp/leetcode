from sys import maxint,maxsize


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

    def minSubArrayLen(self, s, nums):
        sz = len(nums)
        l, total, res = -1, 0, maxsize
        for r in range(0, sz):
            total += nums[r]
            if total >= s:
                while total >= s:
                    l += 1
                    total -= nums[l]
                res = min(res, r+1-l)
        return res if res != maxsize else 0
