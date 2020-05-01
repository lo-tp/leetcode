class Solution(object):
    def findMinArrowShots(self, points):
        res = 0
        if points:
            points.sort()
            t = points[0][1]
            for start, end in points:
                if start > t:
                    res += 1
                    t = end
                else:
                    t = min(end, t)
            res += 1
        return res

