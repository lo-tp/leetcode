class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        res = 0
        if timeSeries:
            s, e = timeSeries[0], timeSeries[0]+duration-1
            for t in timeSeries:
                if t >= s and t <= e:
                    e = t+duration-1
                else:
                    res += e-s+1
                    s, e = t, t+duration-1
            res += e-s+1
        return res

