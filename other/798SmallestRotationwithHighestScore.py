class Solution(object):
    def bestRotation(self, A):
        sz, data = len(A), [0 for _ in A]
        for i, j in enumerate(A):
            w = i-j
            if w >= 0:
                data[0] += 1
                if w + 1 < sz:
                    data[w+1] -= 1
            w += sz
            if i+1 <= w and i+1 < sz:
                data[i+1] += 1
                if w+1 < sz:
                    data[w+1] -= 1
        res, t, te = 0, 0, -1
        for i, j in enumerate(data):
            t += j
            if t > te:
                res = i
                te = t
        return res
