class Solution(object):
    def orangesRotting(self, grid):
        healthy, threatened, v_sz, h_sz, step = 0, set(), len(
            grid), len(grid[0]), 0
        for v in xrange(0, v_sz):
            for h in xrange(0, h_sz):
                if grid[v][h] == 2:
                    grid[v][h] = 0
                    for i, j in [(i, j) for i, j in [(v+1, h), (v-1, h), (v, h+1), (v, h-1)]
                                 if i >= 0 and i < v_sz and j >= 0 and j < h_sz and grid[i][j] == 1]:
                        threatened.add((i, j))
                elif grid[v][h] == 1:
                    healthy += 1
        while threatened:
            step += 1
            healthy -= len(threatened)
            t = set()
            for v, h in threatened:
                grid[v][h] = 0
                for i, j in [(i, j) for i, j in [(v+1, h), (v-1, h), (v, h+1), (v, h-1)]
                             if i >= 0 and i < v_sz and j >= 0 and j < h_sz and grid[i][j] == 1 and (i, j) not in threatened]:
                    t.add((i, j))
            threatened = t
        return step if not healthy else -1
