import heapq
from sys import maxint
from collections import defaultdict


class Solution(object):
    def networkDelayTime(self, times, N, K):
        heap, distances, data = [(0, K-1)], [maxint] * \
            N, defaultdict(lambda: [])
        for source, target, weight in times:
            data[source-1].append((target-1, weight))
        while heap:
            dis, node = heapq.heappop(heap)
            if distances[node] == maxint:
                distances[node] = dis
                for target, weight in data[node]:
                    if distances[target] == maxint:
                        heapq.heappush(heap, (dis+weight, target))
        ret = max(distances)
        return -1 if ret == maxint else ret
