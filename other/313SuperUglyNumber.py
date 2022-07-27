from typing import List, Optional
from heapq import heappop, heappush


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        s = set([1])
        res = 1
        while n:
            res = heappop(heap)
            for p in primes:
                tem = p * res
                if tem not in s:
                    s.add(tem)
                    heappush(heap, tem)
            n -= 1
        return res
