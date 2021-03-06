from collections import defaultdict
class DisjointSet():
    def __init__(self, size):
        self.rep = [i for i in xrange(0, size)]
        self.rank = [1 for i in xrange(0, size)]

    def find(self, t):
        stack = []
        while t != self.rep[t]:
            stack.append(t)
            t = self.rep[t]

        for i in stack:
            self.rep[i] = t
        return t

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        rank_x, rank_y = self.rank[rep_x], self.rank[rep_y]
        if rep_x == rep_y:
            return
        elif rank_x == rank_y:
            self.rank[rep_x] += 1
        elif rank_x < rank_y:
            rep_x, rep_y = rep_y, rep_x
        self.rep[rep_y] = rep_x
class Solution(object):
    def findRedundantDirectedConnectionTLE(self, edges):
        appearance, num = set(), 0
        index = 1
        for input, output in edges:
            if input not in appearance:
                appearance.add(input)
                num += 1
            if output not in appearance:
                appearance.add(output)
                num += 1
            if num == index:
                return [input, output]
            index += 1

    def findRedundantDirectedConnectionWithDisjointSet(self, edges):
        special_node, parent, N = None, {}, len(edges)
        rep, tmp, child = DisjointSet(N+1), 0, [[]
                                                for _ in xrange(0, N+1)]
        for src, dest in edges:
            if dest in parent:
                tmp, special_node = src, dest
            else:
                parent[dest] = src
            child[src].append(dest)
        if special_node:
            child[tmp] = filter(lambda k: k != special_node, child[tmp])
            stack = [i for i in xrange(0, N+1)]
            while stack:
                k = stack.pop()
                for c in child[k]:
                    rep_c, rep_k = rep.find(c), rep.find(k)
                    if rep_c == rep_k:
                        return [parent[special_node], special_node]
                    rep.union(rep_c, rep_k)
            return [tmp, special_node]
        for src, dest in edges:
            rep_a, rep_b = rep.find(src), rep.find(dest)
            if rep_a == rep_b:
                return [src, dest]
            rep.union(rep_a, rep_b)
    def findRedundantDirectedConnectionDoneBetter(self, edges):
        sz = len(edges)
        tem, tmp, parent = None, None, [0 for _ in xrange(0, sz+1)]
        for src, dest in edges:
            if parent[dest]:
                tmp, tem = dest, src
            else:
                parent[dest] = src
        if tmp:
            uf = DisjointSet(sz+1)
            for i in xrange(1, sz+1):
                if parent[i]:
                    uf.union(i, parent[i])
            t = uf.find(1)
            for i in xrange(2, sz+1):
                if uf.find(i) != t:
                    return [parent[tmp], tmp]
            return [tem, tmp]
        else:
            seen = set()
            for src, dest in edges:
                if dest in seen:
                    return [src, dest]
                seen.add(src)


    def findRedundantDirectedConnection(self, edges):
        special_node, N = 0, len(edges)
        parent, child = [[]
                         for _ in xrange(0, N+1)], [[] for _ in xrange(0, N+1)]
        for src, dest in edges:
            parent[dest].append(src)
            child[src].append(dest)
            if len(parent[dest]) == 2:
                special_node = dest
         # todo: when there is no node with two incoming edges
        if not special_node:
            graph = [[] for _ in xrange(0, N+1)]
            for src, dest in edges:
                graph[src].append(dest)
                seen = set()
                stack = graph[src][:]
                while stack:
                    tmp = stack.pop()
                    if tmp not in seen:
                        if tmp == src:
                            return [src, dest]
                        stack.extend(graph[tmp])
                    seen.add(tmp)
        src = parent[special_node][1]
        child[src] = filter(lambda k: k != special_node, child[src])
        appearance, stack = set(), [special_node]
        while stack:
            tem = stack.pop()
            if tem in appearance:
                return [parent[special_node][0], special_node]
            appearance.add(tem)
            stack.extend(child[tem])
        return [src, special_node]

