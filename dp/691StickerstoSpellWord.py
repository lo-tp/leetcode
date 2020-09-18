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

    def minStickers(self, stickers, target):
        t_count, sz, data = Counter(target), len(
            target), [Counter(i) for i in stickers]
        for i in xrange(0, len(data)):
            for j in xrange(0, len(data)):
                if i != j and data[i] & data[j] == data[j]:
                    data[j] = Counter()
        data = [i & t_count for i in data]
        dp, data, t = [-1]*(2**sz), [''.join(i.elements()) for i in data if i
                                     ], [2**i for i in xrange(0, sz)]
        dp[0] = 0
        for state in xrange(0, 2**sz):
            if dp[state] != -1:
                for i in data:
                    now = state
                    for letter in i:
                        for index, c in enumerate(target):
                            if c == letter and (not (now & t[index])):
                                now |= t[index]
                                break
                    if dp[now] == -1 or dp[now] > dp[state]+1:
                        dp[now] = dp[state]+1
        return dp[-1]
