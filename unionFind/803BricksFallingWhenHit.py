class DisjointSet():
    def __init__(self, sz):
        self.data, self.rank, self.size = [i for i in xrange(
            0, sz)], [1 for _ in xrange(0, sz)], [1 for _ in xrange(0, sz)]

    def find(self, x):
        stack = []
        while x != self.data[x]:
            stack.append(x)
            x = self.data[x]
        for i in stack:
            self.data[i] = x
        return x

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            rank_x, rank_y = self.rank[rep_x], self.rank[rep_y]
            if rank_x == rank_y:
                self.rank[rep_x] += 1
            elif rank_x < rank_y:
                rep_y, rep_x = rep_x, rep_y
            self.data[rep_y] = rep_x
            self.size[rep_x] += self.size[rep_y]

    def getSize(self, x):
        return self.size[self.find(x)]


class Solution(object):
    def hitBricksWA(self, grid, hits):
        v_sz, res = len(grid), []
        if v_sz:
            h_sz = len(grid[0])
            data = [[1 for _ in xrange(0, h_sz)] for _ in xrange(0, v_sz)]
            for v, h in hits:
                data[v][h] = 0
                res.append(0)
                for i, j in [(t, te) for t, te in [(v-1, h), (v+1, h), (v, h-1), (v, h+1)]if t >= 0 and t < v_sz and te >= 0 and te < h_sz and grid[t][te] and data[t][te]]:
                    seen, stack1, stack2, flag = set(), [(i, j)], [], True
                    while stack1:
                        tem, temp = stack1.pop()
                        if tem == 0 and grid[tem][temp] and data[tem][temp]:
                            flag = False
                            break
                        seen.add((tem, tem))
                        stack2.append((tem, temp))
                        for t, te in[(t, te) for t, te in [
                                (tem-1, temp), (tem+1, temp), (tem, temp-1), (tem, temp+1)]]:
                            if t >= 0 and t < v_sz and te >= 0 and te < h_sz and grid[t][te] and data[t][te] and (t, te) not in seen:
                                seen.add((t, te))
                                stack1.append((t, te))
                    if flag:
                        res[-1] += len(stack2)
                        for tem, temp in stack2:
                            data[tem][temp] = 0
        return res
    def hitBricks(self, grid, hits):
        res, v_sz, h_sz = [], len(grid), len(grid[0])
        sz = v_sz*h_sz
        seen, ds = set(), DisjointSet(sz+1)
        for i, j in hits:
            grid[i][j] -= 1
        for v in xrange(0, v_sz):
            for h in xrange(0, h_sz):
                if grid[v][h] > 0:
                    q = v*h_sz+h
                    if not v:
                        ds.union(sz, q)
                    for t, te in [(v-1, h), (v, h-1)]:
                        if t >= 0 and t < v_sz and te >= 0 and te < h_sz and grid[t][te] > 0:
                            w = t*h_sz+te
                            ds.union(q, w)
        for tem, temp in hits[::-1]:
            m = ds.getSize(sz)
            grid[tem][temp] += 1
            q = tem*h_sz+temp
            if grid[tem][temp]:
                for t, te in [(tem+1, temp), (tem-1, temp), (tem, temp+1), (tem, temp-1)]:
                    if t >= 0 and t < v_sz and te >= 0 and te < h_sz and grid[t][te] > 0:
                        w = t*h_sz+te
                        ds.union(q, w)
                if not tem:
                    ds.union(sz, q)
            res.append(max(0, ds.getSize(sz)-m-1))
        return res[::-1]
