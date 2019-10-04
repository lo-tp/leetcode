from sys import maxint


class Solution(object):
    def findMinHeightTreesTLE(self, n, edges):
        res, min_height = [], maxint
        data = [[] for _ in xrange(0, n)]
        for src, dest in edges:
            data[src].append(dest)
            data[dest].append(src)
        for i in xrange(0, n):
            visited, height = {i: True}, 1
            stack = [w for w in data[i] if w not in visited]
            while stack:
                tmp = []
                height += 1
                for j in stack:
                    visited[j]=True
                    for k in [k for k in data[j] if k not in visited]:
                        tmp.append(k)
                stack = tmp
            if height < min_height:
                res = [i]
                min_height = height
            elif height == min_height:
                res.append(i)
        return res
    def findMinHeightTrees(self, n, edges):
        data = [[0, []] for _ in xrange(0, n)]
        for src, dest in edges:
            data[src][0] += 1
            data[src][1].append(dest)
            data[dest][0] += 1
            data[dest][1].append(src)
        size = n
        while n > 2:
            for i in [ i for i in xrange(0, size) if data[i][0]==1]:
                data[i][0] = -1
                n -= 1
                for j in data[i][1]:
                    data[j][0] -= 1
        return [i for i in xrange(0, size) if data[i][0] > -1]
