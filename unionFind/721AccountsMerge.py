class DisjointSetWA(object):
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
    def accountsMergeWA(self, accounts):
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
        if t not in self.data:
            self.data[t] = t

    def union(self, x, y):
        t = self.find(y)
        self.data[t if t else y] = self.find(x)


class Solution(object):
    def accountsMerge(self, accounts):
        non_empty, empty, res, data, ds = set(), set(), [], {}, DisjointSet()
        for account in accounts:
            sz = len(account)
            if sz > 1:
                data[account[1]] = (account[0], set())
                ds.insert(account[1])
                for i in xrange(2, sz):
                    ds.union(account[1], account[i])
            else:
                empty.add(account)
        for account in accounts:
            for i in xrange(1, len(account)):
                t = ds.find(account[i])
                non_empty.add(t)
                data[t][1].add(account[i])
        for i in empty:
            res.append([i])
        for i in non_empty:
            name, emails = data[i]
            t = [name]
            t.extend(sorted(emails))
            res.append(t)
        return res


