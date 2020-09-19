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
