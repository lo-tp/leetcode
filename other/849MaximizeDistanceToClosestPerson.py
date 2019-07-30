class Solution(object):
    def maxDistToClosest(self, seats):
        interval, size, data = 0, len(seats), []
        for index, i in enumerate(seats):
            if i:
                data.append(index)
        for i in xrange(1, len(data)):
            interval = max(interval, data[i]-data[i-1])
        return max(data[0], size-data[-1]-1, interval/2)

