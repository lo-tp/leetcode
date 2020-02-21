class Solution(object):
    def trapRainWater(self, H):
        v_sz, res = len(H), 0
        if v_sz:
            h_sz = len(H[0])
            if h_sz:
                stop = False
                while not stop:
                    stop = True
                    seen = set()
                    # print H
                    for h in xrange(0, h_sz):
                        for v in [0, v_sz-1]:
                            stack = [(v, h)]
                            while stack:
                                t, te = stack.pop()
                                if t >= 0 and t < v_sz and te >= 0 and te < h_sz:
                                    id = '{} {}'.format(t, te)
                                    if id not in seen:
                                        seen.add(id)
                                        if H[t][te] <= 0:
                                            H[t][te] = -1
                                            stack.append((t, te+1))
                                            stack.append((t+1, te))
                                            stack.append((t, te-1))
                                            stack.append((t-1, te))
                    for h in [0, h_sz-1]:
                        for v in xrange(1, v_sz-1):
                            stack = [(v, h)]
                            while stack:
                                t, te = stack.pop()
                                if t >= 0 and t < v_sz and te >= 0 and te < h_sz:
                                    id = '{} {}'.format(t, te)
                                    if id not in seen:
                                        seen.add(id)
                                        if H[t][te] <= 0:
                                            H[t][te] = -1
                                            stack.append((t, te+1))
                                            stack.append((t+1, te))
                                            stack.append((t, te-1))
                                            stack.append((t-1, te))
                    for h in xrange(0, h_sz):
                        for v in xrange(0, v_sz):
                            if H[v][h] != -1:
                                if H[v][h]:
                                    stop = False
                                    H[v][h] -= 1
                                else:
                                    res += 1
        # print res
        return res

