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
    def nthSuperUglyNumberWithDP(self, n: int, primes: List[int]) -> int:
        dp = [1]
        res = 1
        index = [0 for i in primes]
        heap = [(primes[i], i) for i in range(0, len(primes))]
        n -= 1
        while n:
            (res, i) = heappop(heap)
            dp.append(res)
            index[i] += 1
            while heap and heap[0][0] == res:
                num, j = heappop(heap)
                index[j] += 1
                heappush(heap, (dp[index[j]] * primes[j], j))
            heappush(heap, (dp[index[i]] * primes[i], i))
            n -= 1
        return res
