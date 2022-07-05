from typing import List
from math import floor


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sz = sum(matchsticks)
        if sz % 4 or matchsticks[0] * 4 > sz:
            return False
        edges = [floor(sz / 4)] * 4
        stack = [(0, 3, False)]
        while stack:
            # print(edges)
            # print(stack)
            index, edgeIndex, flag = stack.pop()
            if not flag:
                edges[edgeIndex] -= matchsticks[index]
                # if not edges[edgeIndex]:
                # print(index, edgeIndex)
                    # print(edges)
                # print(stack)
                # if not sum(edges):
                if len([e for e in edges if e])==3:
                    return True
                stack.append((index, edgeIndex, True))
                index += 1
                for e in range(0, 4):
                    if edges[e] and edges[e] >= matchsticks[index]:
                        stack.append((index, e, False))
                        break
            else:
                edges[edgeIndex] += matchsticks[index]
                for e in range(edgeIndex + 1, 4):
                    if edges[e] and edges[e] >= matchsticks[index]:
                        stack.append((index, e, False))
                        break
        return False
