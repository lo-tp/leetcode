from heapq import heappush
from math import floor
from bisect import bisect_left

class Solution(object):
    def nextGreaterElement(self, n):
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


    def nextGreaterElement(self, n: int) -> int:
        nums = []
        while n:
            nums.append(-(n % 10))
            n = floor(n / 10)
        heap = []
        for i in range(0, len(nums)):
            if heap and heap[0] < nums[i]:
                heap.sort()
                index = bisect_left(heap, nums[i]) - 1
                heap[index], nums[i] = nums[i], heap[index]
                heap.sort()
                nums = [str(-j) for j in heap + nums[i:]]
                nums.reverse()
                res = int("".join(nums))
                if res <2 ** 31:
                    return res
                else:
                    return -1
            heappush(heap, nums[i])
        return -1
