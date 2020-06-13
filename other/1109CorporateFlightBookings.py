class Solution(object):
    def corpFlightBookings(self, bookings, n):
        t, res, data = 0, [], [0 for _ in xrange(0, n+2)]
        for start, end, num in bookings:
            data[start] += num
            data[end+1] -= num
        for i in xrange(1, n+1):
            t += data[i]
            res.append(t)
        return res
