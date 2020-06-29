class Solution(object):
    def containVirus(self, grid):
        res, v_sz, h_sz = 0, len(grid), len(grid[0])
        while True:
            seen, infected, threatened, perimeter, = set(), [], [], []
            for v in xrange(0, v_sz):
                for h in xrange(0, h_sz):
                    if (v, h) not in seen and grid[v][h] == 1:
                        stack = [(v, h)]
                        infected.append(set())
                        threatened.append(set())
                        perimeter.append(0)
                        while stack:
                            i, j = stack.pop()
                            if (i, j) not in seen and grid[i][j] == 1:
                                infected[-1].add((i, j))
                                stack.extend([(w, m) for w, m in [
                                             (i, j+1), (i, j-1), (i+1, j), (i-1, j)] if w >= 0 and w < v_sz and m >= 0 and m < h_sz])
                            elif not grid[i][j]:
                                perimeter[-1] += 1
                                threatened[-1].add((i, j))
                            seen.add((i, j))
            if not infected:
                break
            index = threatened.index(max(threatened, key=len))
            res += perimeter[index]
            for i, j in infected[index]:
                grid[i][j] = -1
            for i, j in enumerate(threatened):
                if i != index:
                    for w, m in j:
                        grid[w][m] = 1
        return res
