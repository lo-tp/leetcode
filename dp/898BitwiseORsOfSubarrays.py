class Solution(object):
    def subarrayBitwiseORsTLE(self, A):
        te, t, seen, sz = set(), 0, set(),  len(A)
        data = [(0, i) for i in xrange(0, sz)]
        while data:
            tmp = []
            for i, j in data:
                id = '{} {}'.format(i, j)
                if id not in te:
                    te.add(id)
                    tem = i | A[j]
                    seen.add(tem)
                    j += 1
                    if j < sz:
                        tmp.add((tem, j))
            data = tmp
        return len(seen)
    def subarrayBitwiseORs(self, A):
        te, t, seen, sz = set(), 0, set(),  len(A)
        data = [(0, i) for i in xrange(0, sz)]
        while data:
            tmp = []
            for i, j in data:
                id = '{} {}'.format(i, j)
                if id not in te:
                    te.add(id)
                    tem = i | A[j]
                    seen.add(tem)
                    j += 1
                    if j < sz:
                        tmp.append((tem, j))
            data = tmp
        return len(seen)
    def subarrayBitwiseORsDoneBetter(self, A):
        seen = set([0])
        res = set()
        for i in A:
            seen = {j | i for j in seen} | {i}
            res |= seen
        return len(res)
