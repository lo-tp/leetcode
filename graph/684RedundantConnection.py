from collections import defaultdict


class Solution(object):
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

