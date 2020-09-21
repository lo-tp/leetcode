class Solution(object):
    def summaryRanges(self, n):
        res, sz = [], len(n)
        if sz:
            s, next = n[0], n[0]+1
            for i in xrange(1, sz):
                if n[i] == next:
                    next += 1
                else:
                    res.append('{}->{}'.format(s, next-1) if s !=
                               next-1 else '{}'.format(s))
                    s = n[i]
                    next = s+1
            res.append('{}->{}'.format(s, next-1) if s !=
                       next-1 else '{}'.format(s))
        return res

