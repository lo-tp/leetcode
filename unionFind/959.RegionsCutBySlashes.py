class Solution(object):
    def regionsBySlashes(self, grid):
        res, sz = 0, len(grid)
        if sz:
            res += 1
            data = set()
            for v in xrange(0, sz+1):
                data.add('{},{}'.format(v, 0))
                data.add('{},{}'.format(v, sz))
            for h in xrange(1, sz):
                data.add('{},{}'.format(0, h))
                data.add('{},{}'.format(sz, h))
            for v, string in enumerate(grid):
                i = 0
                for h in xrange(0, sz):
                    t = 0
                    if string[i] == '/':
                        te = '{},{}'.format(v+1, h)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                        te = '{},{}'.format(v, h+1)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                    elif string[i] == '\\':
                        te = '{},{}'.format(v, h)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                        te = '{},{}'.format(v+1, h+1)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                    i += 1
                    if t == 2:
                        print v, h
                        res += 1
        return res

class DisjointSet():
    def __init__(self, sz):
        self.count = sz
        self.data = [i for i in xrange(0, sz)]
        self.rank = [1 for i in self.data]

    def find(self, target):
        stack = []
        while self.data[target] != target:
            target = self.data[target]
        for i in stack:
            self.data[i] = target
        return target

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        rank_x, rank_y = self.rank[rep_x], self.rank[rep_y]
        if rep_x != rep_y:
            self.count -= 1
            if self.rank[rep_x] < self.rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x
            elif rank_x == rank_y:
                self.rank[rep_x] += 1
            self.data[rep_y] = rep_x

    def getCount(self):
        return self.count


class Solution(object):
    def regionsBySlashes(self, grid):
        sz = len(grid)
        ds = DisjointSet(sz*sz*4)
        for i in xrange(0, sz):
            for j in xrange(0, sz-1):
                t = i*sz+j
                left, right = t*4+2, (t+1)*4
                ds.union(left, right)
                t = j*sz+i
                bottom, top = t*4+3, (t+sz)*4+1
                ds.union(bottom, top)
        index = 0
        for v in xrange(0, sz):
            for h in xrange(0, sz):
                if grid[v][h] == '/':
                    ds.union(index, index+1)
                    ds.union(index+3, index+2)
                elif grid[v][h] == '\\':
                    ds.union(index, index+3)
                    ds.union(index+1, index+2)
                else:
                    ds.union(index, index+1)
                    ds.union(index+2, index+3)
                    ds.union(index, index+3)
                index += 4
        return ds.getCount()
