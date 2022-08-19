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
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sz = len(graph)
        if sz < 2:
            return False
        t = Union(sz)
        for v in range(0, sz):
            for h in graph[v]:
                t.union(v, h)
        if t.count() > 1:
            return False
        s1, s2 = set(), set()
        s1.add(0)
        visited = set()
        visited.add(0)
        stack = [0]
        while stack:
            i = stack.pop()
            tem, temp = s1, s2
            # i is already in tem
            if i in s2:
                tem, temp = temp, tem
            for j in graph[i]:
                if j in tem:
                    return False
                if j not in visited:
                    temp.add(j)
                    visited.add(j)
                    stack.append(j)
        return True
