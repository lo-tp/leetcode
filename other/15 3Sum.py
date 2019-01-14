def qc(arr, start, end):
    s, e, m = start, end, arr[(end-start)/2+start]
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            if arr[s] != arr[e]:
                arr[s] = arr[s] ^ arr[e]
                arr[e] = arr[s] ^ arr[e]
                arr[s] = arr[s] ^ arr[e]
            s += 1
            e -= 1
    if s < end:
        qc(arr, s, end)
    if start < e:
        qc(arr, start, e)
    return arr


class Solution(object):
    def threeSum(self, nums):
        res, sz = [], len(nums)
        if sz >= 3:
            temp = []
            i = 0
            while i < sz-2:
                w = i+1
                while w < sz-1:
                    z = w+1
                    while z < sz:
                        if nums[i]+nums[w]+nums[z] == 0:
                            temp.append([nums[i], nums[w], nums[z]])
                        z += 1
                    w += 1
                i += 1
            temp = map(lambda x: qc(x, 0, 2), temp)
            tmp = {}
            for i in temp:
                tem = '%d %d %d' % (i[0], i[1], i[2])
                if tem not in tmp:
                    res.append(i)
                    tmp[tem] = 0
        return res
