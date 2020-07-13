def qc(arr, start, end):
    s, e, m = start, end, arr[start+(end-start)/2]
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
    def maximumProduct(self, nums):
        qc(nums, 0, len(nums)-1)
        if nums[-1] <= 0 or nums[0] >= 0:
            return nums[-1]*nums[-2]*nums[-3]
        return nums[-1]*max(nums[0]*nums[1], nums[-2]*nums[-3])

