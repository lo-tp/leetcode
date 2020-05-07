from sys import maxint
from collections import deque
from heapq import heapify, heappop, heappush


class Mq:
    def __init__(self):
        self.q = deque()

    def pop(self):
        if self.q[0][1]:
            self.q[0][1] -= 1
        else:
            self.q.popleft()

    def getMax(self):
        return self.q[0][0]

    def push(self, element):
        count = 0
        while len(self.q) and self.q[-1][0] < element:
            count += self.q[-1][1]+1
            self.q.pop()
        self.q.append([element, count])


class Solution(object):
    def maxSlidingWindowBruteForce(self, nums, k):
        res, sz = [], len(nums)
        if sz and k:
            for start in xrange(0, sz-k+1):
                m = -maxint
                for w in xrange(start, start+k):
                    m = max(m, nums[w])
                res.append(m)
        return res

    def maxSlidingWindow(self, nums, k):
        res, sz = [], len(nums)
        if sz and k:
            mq = Mq()
            for i in nums[:k-1]:
                mq.push(i)
            for i in nums[k-1:]:
                mq.push(i)
                res.append(mq.getMax())
                mq.pop()
        return res
    def maxSlidingWindowWithHeap(self, nums, k):
        res, heap = [], []
        for i in xrange(0, k):
            heap.append((-nums[i], i))
        heapify(heap)
        j = 0
        for i in xrange(k, len(nums)):
            res.append(-heap[0][0])
            heappush(heap, (-nums[i], i))
            while heap[0][1] <= j:
                heappop(heap)
            j += 1
        res.append(-heap[0][0])
        return res
