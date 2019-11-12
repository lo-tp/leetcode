class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        if intervals:
            start, end = newInterval
            for s, e in intervals:
                if start != -1:
                    # 1
                    if e < start:
                        res.append([s, e])
                    # 2
                    elif end < s:
                        res.append([start, end])
                        res.append([s, e])
                        start = -1
                    else:
                        start, end = min(start, s), max(end, e)
                else:
                    res.append([s, e])
            if start != -1:
                res.append([start, end])
        else:
            res.append(newInterval)
        return res

