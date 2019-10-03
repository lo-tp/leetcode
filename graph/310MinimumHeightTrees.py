from sys import maxint


class Solution(object):
    def findMinHeightTrees(self, n, edges):
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
