from heapq import heappop, heappush


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
