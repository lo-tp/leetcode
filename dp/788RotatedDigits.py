from typing import List
from math import floor

mapping = {0: 0, 1: 1, 8: 8, 2: 5, 5: 2, 6: 9, 9: 6}


def convert(num: int):
    res = 0
    base = 1
    while num:
        t = num % 10
        if t in mapping:
            res += base * mapping[t]
            num = floor(num / 10)
            base *= 10
        else:
            res = -1
            break
    return res


class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        n += 1
        for i in range(2, n):
            c = convert(i)
            # print(i, c)
            if c != -1 and c != i:
                res += 1
                print(i)
        return res

s = Solution()
print(s.rotatedDigits(200))
