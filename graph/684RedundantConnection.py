from collections import defaultdict

class DisjointSet():
    def __init__(self, size):
        self.rep = [i for i in xrange(0, size)]
        self.rank = [1 for i in xrange(0, size)]

    def find(self, target):
        stack = []
        while target != self.rep[target]:
            target = self.rep[target]

        for i in stack:
            self.rep[i] = target

        return target

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            rank_x, rank_y = self.rank[rep_x],  self.rank[rep_y]
            if rank_x == rank_y:
                self.rank[rank_x] += 1
            elif rank_x < rank_y:
                rep_x, rep_y = rep_y, rep_x
            self.rep[rep_y] = rep_x


class Solution(object):
    def findRedundantConnectionWithDisjointSet(self, edges):
        ds = DisjointSet(len(edges)+1)
        for src, dest in edges:
            rep_s, rep_d = ds.find(src), ds.find(dest)
            if rep_s == rep_d:
                return [src, dest]
            ds.union(rep_s, rep_d)
    def findRedundantConnection(self, edges):
        graph = [[] for _ in edges]
        graph.append([])
        for src, dest in edges:
            if src == dest:
                return [src, dest]
            graph[src].append(dest)
            graph[dest].append(src)
            stack = filter(lambda k: k != dest, graph[src])
            seen = set()
            seen.add(src)
            while stack:
                t = stack.pop()
                if t not in seen:
                    if t == dest:
                        return [src, dest]
                    stack.extend(graph[t])
                seen.add(t)

