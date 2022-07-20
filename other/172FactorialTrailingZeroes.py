from typing import List, Optional
from math import floor


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        for i in range(5, n + 1):
            if not i % 10:
                while not i % 10:
                    # print(i)
                    res += 1
                    i = floor(i / 10)
            if not i % 5:
                while not i % 5:
                    # print(i)
                    res += 1
                    i = floor(i / 5)
        return res

    def trailingZeroesBetter(self, n: int) -> int:
        res = 0
        while n:
            n = floor(n / 5)
            res += n
        return res
