from typing import List, Optional


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res, vSz, hSz = 0, len(grid), len(grid[0])
        stack = (
            [(0, h, False) for h in range(1, hSz - 1)]
            + [(vSz - 1, h, False) for h in range(1, hSz - 1)]
            + [(v, 0, False) for v in range(1, vSz - 1)]
            + [(v, hSz - 1, False) for v in range(1, vSz - 1)]
            + [
                (0, 0, False),
                (0, hSz - 1, False),
                (vSz - 1, 0, False),
                (vSz - 1, hSz - 1, False),
            ]
        )
        t = 0
        while stack:
            v, h, flag = stack.pop()
            if flag:
                if not v or not h or v == vSz - 1 or h == hSz - 1:
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
