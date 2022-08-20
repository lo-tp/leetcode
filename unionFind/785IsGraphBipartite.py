from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sz = len(graph)
        s1, s2 = set(), set()
        visited = set()
        for i in range(0, sz):
            if i not in visited:
                s1.add(i)
                visited.add(i)
                stack = [i]
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
