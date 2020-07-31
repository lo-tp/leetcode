from sys import maxint


class Solution(object):
    def calculateMinimumHP(self, d):
        v_sz, h_sz, stack, res = len(d), len(
            d[0]), [(0, 0, 1+(d[0][0] if d[0][0] > 0 else 0), 1 - (0 if d[0][0] > 0 else d[0][0]))], maxint

        while stack:
            v, h, current, minimum = stack.pop()
            if minimum >= res:
                continue
            if v == v_sz-1 and h == h_sz-1:
                res = min(res, minimum)

            for t, te in [(t, te) for t, te in (v+1, h), (v, h+1) if t < v_sz and te < h_sz]:
                c = current+d[t][te]
                stack.append((t, te, max(c, 1), minimum-(0 if c > 0 else c-1)))
        return res
