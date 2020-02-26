from heapq import heappush, heapify, heappop

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

    def trapRainWater(self, H):
        res, v_sz = 0, len(H)
        if v_sz:
            h_sz = len(H[0])
            if h_sz:
                t, self.data = -1, []
                for h in xrange(0, h_sz):
                    self.data.append((H[0][h], 0, h))
                    self.data.append((H[v_sz-1][h], v_sz-1, h))
                    H[0][h] = -1
                    H[v_sz-1][h] = -1
                for v in xrange(1, v_sz-1):
                    self.data.append((H[v][0], v, 0))
                    self.data.append((H[v][h_sz-1], v, h_sz-1))
                    H[v][0] = -1
                    H[v][h_sz-1] = -1
                heapify(self.data)
                while self.data:
                    i, v, h = heappop(self.data)
                    if i < t:
                        res += t-i
                    else:
                        t = i
                    if v+1 < v_sz and H[v+1][h] != -1:
                        heappush(self.data, (H[v+1][h], v+1, h))
                        H[v+1][h] = -1
                    if h+1 < h_sz and H[v][h+1] != -1:
                        heappush(self.data, (H[v][h+1], v, h+1))
                        H[v][h+1] = -1
                    if v-1 > -1 and H[v-1][h] != -1:
                        heappush(self.data, (H[v-1][h], v-1, h))
                        H[v-1][h] = -1
                    if h-1 > -1 and H[v][h-1] != -1:
                        heappush(self.data, (H[v][h-1], v, h-1))
                        H[v][h-1] = -1
        return res
