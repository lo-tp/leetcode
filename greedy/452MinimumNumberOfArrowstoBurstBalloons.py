from sys import maxint
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

    def findMinArrowShotsBetter(self, points):
        res, t = 0, -maxint
        for start, end in sorted(points, key=lambda x: x[1]):
            if start > t:
                res += 1
                t = end
        return res
