class Solution(object):
    def maximumSumTLE(self, arr):
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
    def maximumSum(self, arr):
        res, sub, non_sub = arr[0], 0, arr[0]
        for i in xrange(1, len(arr)):
            sub = max(non_sub, sub+arr[i])
            non_sub = max(0, non_sub)+arr[i]
            res = max(res, sub, non_sub)
        return res
    def maximumSum(self, arr):
        res, sub, non_sub = arr[0], -arr[0], -1
        for j, i in enumerate(arr):
            sub = max(non_sub, sub+i)
            non_sub = max(0, non_sub)+i
            if j:
                res = max(res, sub, non_sub)
        return res

