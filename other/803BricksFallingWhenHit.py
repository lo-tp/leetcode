class Solution(object):
    def hitBricks(self, grid, hits):
        v_sz, res = len(grid), []
        if v_sz:
            h_sz = len(grid[0])
            data = [[1 for _ in xrange(0, h_sz)] for _ in xrange(0, v_sz)]
            for v, h in hits:
                data[v][h] = 0
                res.append(0)
                for i, j in [(t, te) for t, te in [(v-1, h), (v+1, h), (v, h-1), (v, h+1)]if t >= 0 and t < v_sz and te >= 0 and te < h_sz and grid[t][te] and data[t][te]]:
                    seen, stack1, stack2, flag = set(), [(i, j)], [], True
                    while stack1:
                        tem, temp = stack1.pop()
                        if tem == 0 and grid[tem][temp] and data[tem][temp]:
                            flag = False
                            break
                        seen.add((tem, tem))
                        stack2.append((tem, temp))
                        for t, te in[(t, te) for t, te in [
                                (tem-1, temp), (tem+1, temp), (tem, temp-1), (tem, temp+1)]]:
                            if t >= 0 and t < v_sz and te >= 0 and te < h_sz and grid[t][te] and data[t][te] and (t, te) not in seen:
                                seen.add((t, te))
                                stack1.append((t, te))
                    if flag:
                        res[-1] += len(stack2)
                        for tem, temp in stack2:
                            data[tem][temp] = 0
        return res
