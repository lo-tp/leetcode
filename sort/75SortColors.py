def qc(arr, start, end):
    if start >= end:
        return
    s, e = start, end
    m = arr[s+(e-s)/2]
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    if s < end:
        qc(arr, s, end)
    if start < e:
        qc(arr, start, e)


class Solution(object):
    def sortColors(self, nums):
        qc(nums, 0, len(nums)-1)
