from collections import defaultdict


class Solution(object):
    def largestOverlap(self, img1, img2):
        res, data1, data2, sz = defaultdict(lambda: 0), [], [], len(img1)
        for v in xrange(0, sz):
            for h in xrange(0, sz):
                if img1[v][h]:
                    data1.append((v, h))
                if img2[v][h]:
                    data2.append((v, h))
        for v1, h1 in data1:
            for v2, h2 in data2:
                res[(v1-v2, h1-h2)] += 1
        return max(res.values()) if res else 0
    def largestOverlap(self, img1, img2):
        res, sz = 0, len(img1)
        data = [[0 for _ in xrange(0, 3*sz-2)] for _ in xrange(0, 3*sz-2)]
        t = sz-1
        for v in xrange(0, sz):
            for h in xrange(0, sz):
                data[t+v][t+h] = img1[v][h]
        for v1 in xrange(2*sz-1):
            for h1 in xrange(2*sz-1):
                t = 0
                for v in xrange(0, sz):
                    for h in xrange(0, sz):
                        if data[v1+v][h1+h] and img2[v][h]:
                            t += 1
                res = max(res, t)
        return res
