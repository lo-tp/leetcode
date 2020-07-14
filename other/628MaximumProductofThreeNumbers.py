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
        min_q,max_q=nums[:2],nums[:3]
        sort(min_q, 0, 1)
        sort(max_q, 0, 2)
        for i in xrange(2, len(nums)):
            if nums[i]<min_q[-1]:
                min_q[-1]=nums[i]
                sort(min_q, 0, 1)
            if nums[i]>max_q[-1]:
                max_q[-1]=nums[i]
                sort(max_q, 0,2)
        return max_q[-1]*max(min_q[0]*min_q[1], max_q[0]*max_q[1])

    def maximumProduct(self, nums):
        min_q, max_q = nums[:3], nums[:3]
        qc(min_q, 0, 2)
        qc(max_q, 0, 2)
        for i in xrange(3, len(nums)):
            if nums[i] < min_q[-1]:
                min_q[-1] = nums[i]
                qc(min_q, 0, 2)
            if nums[i] > max_q[0]:
                max_q[0] = nums[i]
                qc(max_q, 0, 2)
        return max_q[-1]*max(min_q[0]*min_q[1], max_q[0]*max_q[1])
