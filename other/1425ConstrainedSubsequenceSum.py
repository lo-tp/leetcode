from heapq import heappop, heappush
from collections import deque


class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        res, l = nums[0], -(k+1)
        data = [(0, l+1)]
        for r in xrange(0, len(nums)):
            while data[0][1] <= l:
                heappop(data)
            t = nums[r]-data[0][0]
            res = max(t, res)
            heappush(data, (-t, r))
            l += 1
        return res
    def constrainedSubsetSum(self, nums, k):
        res, l = nums[0], -(k+1)
        data = [(0, l+1)]
        for r in xrange(0, len(nums)):
            while data[0][1] <= l:
                heappop(data)
            t = nums[r]-min(0, data[0][0])
            res = max(t, res)
            heappush(data, (-t, r))
            l += 1
        return res
    def constrainedSubsetSumWithDeque(self, nums, k):
        res, l = nums[0], -(k+1)
        data = deque([(0, l+1)])
        for r in xrange(0, len(nums)):
            while data[0][1] <= l:
                data.popleft()
            t = nums[r]+max(0, data[0][0])
            res = max(t, res)
            while data and data[-1][0] < t:
                data.pop()
            data.append((t, r))
            l += 1
        return res

