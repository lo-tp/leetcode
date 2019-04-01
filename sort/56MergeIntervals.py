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


class Solution(object):
    def merge(self, intervals):
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
