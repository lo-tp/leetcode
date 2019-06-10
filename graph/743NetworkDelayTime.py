import heapq
from sys import maxint
from collections import defaultdict, deque

class Heap():
    def __init__(self):
        self.data = deque()
        self.length = 0

    def push(self, ele):
        self.data.append(ele)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.data.popleft()

    def heapify(self):
        if self.length > 1:
            index = (self.length-2)/2
            while index >= 0:
                min_index = index*2+1
                right_index = min_index+1
                if right_index < self.length and self.data[right_index][0] < self.data[min_index][0]:
                    min_index = right_index
                if self.data[min_index][0] < self.data[index][0]:
                    self.data[min_index], self.data[index] = self.data[index], self.data[min_index]
                index -= 1

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
    def networkDelayTimeWithOwnHeapImplementation(self, times, N, K):
        heap, distances, data = Heap(), [maxint] * \
            N, defaultdict(lambda: [])
        heap.push((0, K-1))
        for source, target, weight in times:
            data[source-1].append((target-1, weight))
        while heap.length:
            dis, node = heap.pop()
            if distances[node] == maxint:
                distances[node] = dis
                for target, weight in data[node]:
                    if distances[target] == maxint:
                        heap.push((dis+weight, target))
            heap.heapify()
        ret = max(distances)
        return -1 if ret == maxint else ret
