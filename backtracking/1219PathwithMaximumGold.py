from typing import List, Optional


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res, vSz, hSz = 0, len(grid), len(grid[0])
        stack = []
        for v in range(0, vSz):
            for h in range(0, hSz):
                stack.append((v, h, False))
        t = 0
        while stack:
            v, h, flag = stack.pop()
            if flag:
                res = max(res, t)
                t += grid[v][h]
                grid[v][h] *= -1
            elif grid[v][h] > 0:
                t += grid[v][h]
                grid[v][h] *= -1
                stack.append((v, h, True))
                if v + 1 < vSz:
                    stack.append((v + 1, h, False))
                if h + 1 < hSz:
                    stack.append((v, h + 1, False))
                if v - 1 >= 0:
                    stack.append((v - 1, h, False))
                if h - 1 >= 0:
                    stack.append((v, h - 1, False))
        return res

