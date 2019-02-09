from sys import maxint
from collections import deque


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
