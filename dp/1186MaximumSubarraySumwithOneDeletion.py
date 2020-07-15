class Solution(object):
    def maximumSum(self, arr):
        res, sums, minimums, sz = arr[0], [], [], 0
        for i in arr:
            for j in xrange(0, sz):
                sums[j] += i
                minimums[j] = min(minimums[j], i)
            sums.append(i)
            minimums.append(i)
            for j in xrange(0, sz):
                res = max(res, sums[j], sums[j]-minimums[j])
            res = max(res, sums[sz])
            sz += 1
        return res

