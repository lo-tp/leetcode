from collections import deque

class Solution(object):
    def longestSubarrayTLE(self, nums, limit):
        minimum, maximum, l, res = nums[0], nums[0], 0, 0
        for r in xrange(0, len(nums)):
            maximum = max(maximum, nums[r])
            minimum = min(minimum, nums[r])
            if maximum-minimum > limit:
                while l <= r:
                    l += 1
                    t = nums[l:r+1]
                    maximum, minimum = max(t), min(t)
                    if maximum-minimum <= limit:
                        break
            res = max(r-l+1, res)
        return res

    def longestSubarray(self, nums, limit):
        res, min_q, max_q, l = 0, deque(), deque(), 0
        for r in xrange(0, len(nums)):
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            min_q.append(nums[r])
            max_q.append(nums[r])
            while max_q[0]-min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                elif min_q[0] == nums[l]:
                    min_q.popleft()
                l += 1
            res = max(res, r-l+1)
        return res

    def longestSubarray(self, nums, limit):
        res, l, max_h, min_h = 1, 0, [], []
        for r in xrange(0, len(nums)):
            heappush(max_h, (-nums[r], r))
            heappush(min_h, (nums[r], r))
            while -max_h[0][0]-min_h[0][0] > limit:
                while max_h[0][1] <= l:
                    heappop(max_h)
                while min_h[0][1] <= l:
                    heappop(min_h)
                l += 1
            res = max(res, r-l+1)
        return res

