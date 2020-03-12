from heapq import heappush, heappop, heapify


def mergeSort(arr):
    sz = len(arr)
    if sz > 1:
        res, l, r, l_index, r_index = [], arr[:sz/2], arr[sz/2:], 0, 0
        l_sz, r_sz = len(l), len(r)
        l = mergeSort(l)
        r = mergeSort(r)
        while l_index < l_sz and r_index < r_sz:
            if l[l_index] < r[r_index]:
                res.append(l[l_index])
                l_index += 1
            else:
                res.append(r[r_index])
                r_index += 1
        while l_index < l_sz:
            res.append(l[l_index])
            l_index += 1
        while r_index < r_sz:
            res.append(r[r_index])
            r_index += 1
        return res
    return arr[:]


class Solution(object):
    def medianSlidingWindowTLE(self, nums, k):
        sz, te, res, data = len(nums), k/2, [], nums[:k]
        for i in xrange(k, sz+1):
            t = i % k
            sorted = mergeSort(data)
            res.append(sorted[te] if k % 2 else (sorted[te]+sorted[te-1])/2.0)
            if i < sz:
                data[t] = nums[i]
        return res

    def medianSlidingWindow(self, nums, k):
        res, is_odd, l, r, sz = [], k % 2, [], [], len(nums)
        for i in xrange(0, k):
            l.append((-nums[i], i))
        heapify(l)
        print l
        for _ in xrange(0, k/2):
            t, te = heappop(l)
            r.append((-t, te))
        heapify(r)
        for i in xrange(k, sz):
            j = i - k
            res.append(-l[0][0] if is_odd else (r[0][0]-l[0][0])/2.0)
            print l
            print r
            if nums[i] > r[0][0]:
                heappush(r, (nums[i], i))
                if nums[j] <= r[0][0]:
                    t, te = heappop(r)
                    heappush(l, (-t, te))
            else:
                heappush(l, (-nums[i], i))
                if nums[j] >= r[0][0]:
                    t, te = heappop(l)
                    heappush(r, (-t, te))
            while l and l[0][1] <= j:
                heappop(l)
            while r and r[0][1] <= j:
                heappop(r)
        res.append(-l[0][0] if is_odd else (r[0][0]-l[0][0])/2.0)
        return res
