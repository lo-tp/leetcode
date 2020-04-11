class Solution(object):
    def numberOfSubstrings(self, s):
        res, t, te, data = 0, 0, {
            'a': 0, 'b': 1, 'c': 2}, [0, 0, 0]
        for r in s:
            l = 0
            if not data[te[r]]:
                t += 1
            data[te[r]] += 1
            if t == 3:
                tmp = [0, 0, 0]
                while tmp[te[s[l]]] != data[te[s[l]]]-1:
                    tmp[te[s[l]]] += 1
                    l += 1
                    res += 1
                res += 1
        return res
