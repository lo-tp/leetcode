from collections import Counter


class Solution(object):
    def minStickers(self, stickers, target):
        res, data, t_count, sz = 0, [
            Counter(i).items() for i in stickers], Counter(target), len(target)
        while True:
            i, t = -1, 0
            for index, j in enumerate(data):
                te = 0
                for key, val in j:
                    if key in t_count and t_count[key]:
                        te += min(val, t_count[key])
                if te > t:
                    i, t = index, te
            if not t:
                break
            res += 1
            sz -= t
            for key, val in data[i]:
                if key in t_count:
                    t_count[key] -= min(t_count[key], val)
        return -1 if sz else res

