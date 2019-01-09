def qc(arr, start, end):
    m, l, r = arr[start+(end-start)/2], start, end
    while l <= r:
        while arr[l] > m:
            l += 1
        while arr[r] < m:
            r -= 1
        if l <= r:
            if arr[l] != arr[r]:
                arr[l] = arr[l] ^ arr[r]
                arr[r] = arr[l] ^ arr[r]
                arr[l] = arr[l] ^ arr[r]
            l += 1
            r -= 1
    if l < end:
        qc(arr, l, end)
    if r > start:
        qc(arr, start, r)


class Solution(object):
    def leastInterval(self, tasks, n):
        data = {}
        for i in tasks:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        data = data.values()
        res, sz = 0, len(data)
        if sz:
            qc(data, 0, sz-1)
            while data[0]:
                i = 1
                data[0] -= 1
                res += 1
                while i <= n:
                    if i < sz and data[i]:
                        data[i] -= 1
                        res += 1
                    elif data[0]:
                        res += 1
                    else:
                        break
                    i += 1
                qc(data, 0, sz-1)
        return res


s = Solution()
print s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
print s.leastInterval([], 2)
print s.leastInterval(['A'], 2)
