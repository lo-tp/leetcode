from sys import maxsize
from math import floor, ceil

def dp(n: int):
    if n == 1:
        return 0
    elif n%2:
        return min(dp(ceil(n/2)), dp(floor(n/2))) + 2
    return dp(floor(n/2))+1




class Solution(object):
    def nextGreaterElementMLE(self, n):
        ord_0, seen, data = ord('0'), [0]*10, list(str(n))
        sz = len(data)

        def getIndex(num):
            return ord(num)-ord_0

        seen[getIndex(data[-1])] += 1
        for i in range(sz-2, -1, -1):
            index = getIndex(data[i])
            seen[index] += 1
            for j in range(index+1, 10):
                if seen[j]:
                    seen[j] -= 1
                    data[i] = '{}'.format(j)
                    i, start = 0, i+1
                    for j in range(start, sz):
                        while not seen[i]:
                            i += 1
                        data[j] = '{}'.format(i)
                        seen[i] -= 1
                    res = int(''.join(data))
                    if res < 1 << 31:
                        return res
                    return -1
        return -1

    def integerReplacement(self, n: int) -> int:
        return dp(n)
