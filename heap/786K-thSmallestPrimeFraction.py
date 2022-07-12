from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in arr:
            for j in arr:
                if i != j:
                    t = -i / j
                    if len(heap) < k:
                        heappush(heap,(t, i, j))
                    elif t > heap[0][0]:
                        heappop(heap)
                        heappush(heap,(t, i, j))
        return [heap[0][1], heap[0][2]]
