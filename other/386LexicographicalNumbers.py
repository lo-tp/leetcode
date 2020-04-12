def isASmallerThanB(a, b):
    res, sz_a, sz_b = False, len(a), len(b)
    if sz_a < sz_b:
        res = True
    for i in xrange(0, min(sz_a, sz_b)):
        if a[i] < b[i]:
            res = True
            break
        elif a[i] > b[i]:
            res = False
            break
    return res


def qc(arr, start, end):
    s, e, m = start, end, arr[start+(end-start)/2]
    while s <= e:
        while isASmallerThanB(arr[s], m):
            s += 1
        while isASmallerThanB(m, arr[e]):
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
    def lexicalOrderTLE(self, n):
        res = [str(i) for i in xrange(1, n+1)]
        qc(res, 0, n-1)
        return [int(i) for i in res]


