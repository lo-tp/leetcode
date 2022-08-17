from typing import List


class Union:
    def __init__(self, sz: int):
        self.sz = sz
        self.weight = [0] * sz
        self.parent = [i for i in range(0, sz)]

    def count(self):
        return self.sz

    def find(self, n: int):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def union(self, x: int, y: int):
        pX, pY = self.find(x), self.find(y)
        if pX != pY:
            if self.weight[pX] < self.weight[pY]:
                pX, pY = pY, pX
            self.parent[pY] = pX
            self.weight[pX] += self.weight[pY]
            self.sz -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        sz = len(stones)
        u = Union(sz)
        data = [[] for _ in range(0, sz)]
        for i in range(0, sz):
            v, h = stones[i]
            data[v].append(i)
        for d in data:
            if len(d) > 1:
                for i in range(1, len(d)):
                    u.union(d[0], d[i])
        data = [[] for _ in range(0, sz)]
        for i in range(0, sz):
            v, h = stones[i]
            data[h].append(i)
        for d in data:
            if len(d) > 1:
                for i in range(1, len(d)):
                    u.union(d[0], d[i])
        return sz - u.count()
