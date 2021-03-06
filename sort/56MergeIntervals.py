def heapify(arr, end):
    if end:
        m = (end-1)/2
        while m >= 0:
            minIndex = m*2+1
            rightIndex = minIndex+1
            if rightIndex <= end and arr[rightIndex].start > arr[minIndex].start:
                minIndex = rightIndex
            if arr[minIndex].start > arr[m].start:
                arr[m], arr[minIndex] = arr[minIndex], arr[m]
            m -= 1


def sort(arr):
    end = len(arr)-1
    while end:
        heapify(arr, end)
        arr[0], arr[end] = arr[end], arr[0]
        end -= 1


def compare(a, b):
    if a.start < b.start or (a.start == b.start and a.end < b.end):
        return -1
    elif a.start == b.start and a.end == b. end:
        return 0
    return 1


class Solution(object):
    def merge(self, intervals):
        if intervals:
            i, sz, res = 0, len(intervals), []
            list.sort(cmp=compare)
            while i < sz:
                w = intervals[i].end
                e = i+1
                while e < sz and w >= intervals[e].start:
                    w = max(w, intervals[e].end)
                    e += 1
                res.append(Interval(intervals[i].start, w))
                i = e
            return res
        return intervals
    def mergeTLE(self, intervals):
        if intervals:
            i, sz, res = 0, len(intervals), []
            sort(intervals)
            while i < sz:
                w=i.end
                e = i+1
                while e < sz and w >= intervals[e].start:
                    e += 1
                res.append(Interval(intervals[i].start, intervals[e-1].end))
                i = e
            return res
        return intervals
    def mergeBetter(self, intervals):
        res = []
        if intervals:
            tmp = sorted(intervals)
            t = tmp[0][1]
            res.append(tmp[0])
            for start, end in tmp:
                if start > t:
                    res[-1][1] = t
                    res.append([start, 0])
                t = max(t, end)
            res[-1][1] = t
        return res

