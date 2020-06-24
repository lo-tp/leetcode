from heapq import heappop, heappush

class MedianFinder(object):

    def __init__(self):
        self.l, self.r = [], []

    def addNum(self, num):
        if not self.l and not self.r:
            heappush(self.r, num)
        elif num >= self.r[0]:
            heappush(self.r, num)
            if len(self.r)-1 > len(self.l):
                heappush(self.l, -heappop(self.r))
        else:
            heappush(self.l, -num)
            if len(self.l) > len(self.r):
                heappush(self.r, -heappop(self.l))

    def findMedian(self):
        return self.r[0] if (len(self.l)+len(self.r)) % 2 else (self.r[0]-self.l[0])/2.0

