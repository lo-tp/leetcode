from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        sz = len(arr)
        for i in range(1, sz):
            heappush(heap, (arr[0] / arr[i], 0, i))
        k -= 1
        while k:
            _, i, j = heappop(heap)
            if i + 1 < j:
                i += 1
                heappush(heap, (arr[i] / arr[j], i, j))
            k -= 1
        return [arr[heap[0][1]], arr[heap[0][2]]]
