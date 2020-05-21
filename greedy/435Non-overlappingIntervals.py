from sys import maxint


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        t, res, tmp = -maxint, 0, sorted(intervals)
        for start, end in tmp:
            if start < t:
                res += 1
                t = min(end, t)
            else:
                t = end
        return res


