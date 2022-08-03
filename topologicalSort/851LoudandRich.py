from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        sz = len(quiet)
        visited = [False] * sz
        graph = [[] for _ in range(0, sz)]
        for target, source in richer:
            graph[source].append(target)
        res = [0] * sz
        for i in range(0, sz):
            stack = [(i, False)]
            res[i] = i
            q = quiet[i]
            while stack:
                index, flag = stack.pop()
                if flag:
                    if quiet[index] < q:
                        q = quiet[index]
                        res[i] = index
                else:
                    stack.append((index, True))
                    stack.extend([(i, False) for i in graph[index]])
        return res
