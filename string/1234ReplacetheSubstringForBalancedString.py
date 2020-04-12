from collections import Counter


class Solution(object):
    def balancedStringWA(self, s):
        sz, t = len(s), Counter(s)
        res, l, te, data = 0, 0, sz/4, {}
        for i in t:
            if t[i] > te:
                data[i] = t[i]-te
        if data:
            res = sz
            for r in xrange(0, sz):
                if s[r] in data:
                    data[s[r]] -= 1
                for i in data:
                    while data[i] < 0:
                        if s[l] in data:
                            data[s[l]] += 1
                        l += 1
                while s[l] not in data:
                    l += 1
                flag = True
                for j in data:
                    if data[j]:
                        flag = False
                        break
                if flag:
                    res = min(res, r-l+1)
        return res

    def balancedString(self, s):
        sz, count, l = len(s), Counter(s), 0
        res, t = sz, sz/4
        for r in xrange(0, sz):
            count[s[r]] -= 1
            while l < sz and max(count.values()) <= t:
                res = min(res, r-l+1)
                count[s[l]] += 1
                l += 1
        return res

