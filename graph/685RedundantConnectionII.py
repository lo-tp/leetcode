from collections import defaultdict
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

