from copy import copy


class Solution(object):
    def uniquePathsIII(self, grid):
        to_visit, start, end, count, res, h_sz, v_sz = set(), None, None, 0, 0, len(
            grid[0]), len(grid)

        for v in xrange(0, v_sz):
            for h in xrange(0, h_sz):
                if grid[v][h] == -1:
                    continue
                count += 1
                to_visit.add((v, h))
                if grid[v][h] == 1:
                    start = (v, h)
                elif grid[v][h] == 2:
                    end = (v, h)

        stack = [(start, [(start[0], start[1])], set(start))]
        while stack:
            t, path, visited = stack.pop()
            if t == end and len(visited) == count:
                res += 1
            for v, h in [(v, h) for v, h in [(t[0]+1, t[1]), (t[0]-1, t[1]), (t[0], t[1]+1), (t[0], t[1]-1)] if v >= 0 and v < v_sz and h >= 0 and h < h_sz and (v, h) not in visited and (v, h) in to_visit]:
                new_visited, new_path = copy(visited), path[:]
                new_visited.add((v, h))
                path.append((v, h))
                stack.append(((v, h), new_path, new_visited))
        return res

    def uniquePathsIII(self, grid):
        to_visit, start, end, count, res, h_sz, v_sz = set(), None, None, 0, 0, len(
            grid[0]), len(grid)

        for v in xrange(0, v_sz):
            for h in xrange(0, h_sz):
                if grid[v][h] == -1:
                    continue
                count += 1
                to_visit.add((v, h))
                if grid[v][h] == 1:
                    start = (v, h)
                elif grid[v][h] == 2:
                    end = (v, h)

        stack = [(start, [(start[0], start[1])], set())]
        stack[-1][-1].add(start)
        while stack:
            t, path, visited = stack.pop()
            if t == end and len(visited) == count:
                res += 1
            for v, h in [(v, h) for v, h in [(t[0]+1, t[1]), (t[0]-1, t[1]), (t[0], t[1]+1), (t[0], t[1]-1)] if v >= 0 and v < v_sz and h >= 0 and h < h_sz and (v, h) not in visited and (v, h) in to_visit]:
                new_visited, new_path = copy(visited), path[:]
                new_visited.add((v, h))
                path.append((v, h))
                stack.append(((v, h), new_path, new_visited))
        return res
    def uniquePathsIII(self, grid):
        self.v_sz, self.h_sz, num, self.grid = len(grid), len(grid[0]), 0, grid
        start_v, start_h = None, None
        for v in xrange(0, self.v_sz):
            for h in xrange(0, self.h_sz):
                if grid[v][h] != -1:
                    num += 1
                if grid[v][h] == 1:
                    start_v, start_h = v, h

        return self.dfs(num, start_v, start_h)

    def dfs(self, num, v, h):
        num -= 1
        if self.grid[v][h] == -1:
            return 0
        if self.grid[v][h] == 2:
            return 0 if num else 1

        res, self.grid[v][h] = 0, -1
        v += 1
        if v < self.v_sz:
            res += self.dfs(num, v, h)
        v -= 2
        if v > -1:
            res += self.dfs(num, v, h)
        v += 1
        h += 1
        if h < self.h_sz:
            res += self.dfs(num, v, h)
        h -= 2
        if h > -1:
            res += self.dfs(num, v, h)
        h += 1
        self.grid[v][h] = 0
        return res

