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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        sz = len(isConnected)
        u = Union(sz)
        for x in range(0, sz):
            for y in range(0, sz):
                if isConnected[x][y]:
                    u.union(x, y)
        return u.count()
