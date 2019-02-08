from sys import maxint


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res, sz = [], len(nums)
        if sz and k:
            for start in xrange(0, sz-k+1):
                m = -maxint
                for w in xrange(start, start+k):
                    m = max(m, nums[w])
                res.append(m)
        return res
