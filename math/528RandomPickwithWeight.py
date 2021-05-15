from random import randrange


class Solution(object):

    def __init__(self, w):
        self.prefix_sum, self.sz, self.total = [], len(w), 0
        for n in w:
            self.total += n
            self.prefix_sum.append(self.total)

    def pickIndex(self):
        t = randrange(0, self.total)
        if t < self.prefix_sum[0]:
            return 0
        l, r = 1, self.sz-1
        while True:
            m = l+(r-l)/2
            if t >= self.prefix_sum[m]:
                l = m+1
            elif t < self.prefix_sum[m-1]:
                r = m-1
            else:
                return m
