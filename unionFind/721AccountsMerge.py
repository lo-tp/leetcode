class DisjointSet(object):
    def __init__(self):
        self.data = {}

    def find(self, t):
        if t in self.data:
            s = []
            while t != self.data[t]:
                s.append(t)
                t = self.data[t]
            for i in s:
                self.data[i] = t
            return t
        return None

    def insert(self, t):
        self.data[t] = t

    def union(self, x, y):
        self.data[y] = self.data[x]


class Solution(object):
    def accountsMerge(self, accounts):
        data, res, ds = {}, [], DisjointSet()
        for t in accounts:
            sz = len(t)
            if sz > 1:
                flag, te = None, []
                for i in xrange(1, sz):
                    te.append(t[i])
                    tem = ds.find(t[i])
                    if tem:
                        flag = tem
                if flag:
                    te = set(te)
                    for i in te:
                        ds.union(flag, i)
                        name, emails = data[flag]
                        data[flag] = (name, emails | te)
                else:
                    te, flag = set(te), te[0]
                    ds.insert(flag)
                    for i in te:
                        ds.union(flag, i)
                    data[flag] = (t[0], te)
            else:
                res.append(t)

        for name, emails in data.values():
            te = [name]
            te.extend(sorted(list(emails)))
            res.append(te)
        return res
