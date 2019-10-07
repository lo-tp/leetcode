def mg(arr):
    size = len(arr)
    if size > 1:
        m = size/2
        l, r, index, l_index, r_index = arr[:m], arr[m:], 0, 0, 0
        l_size, r_size = len(l), len(r)
        mg(l)
        mg(r)
        while l_index < l_size and r_index < r_size:
            if l[l_index] < r[r_index]:
                arr[index] = l[l_index]
                l_index += 1
            else:
                arr[index] = r[r_index]
                r_index += 1
            index += 1
        while l_index < l_size:
            arr[index] = l[l_index]
            index += 1
            l_index += 1
        while r_index < r_size:
            arr[index] = r[r_index]
            index += 1
            r_index += 1


def qs(arr, start, end):
    if end > start:
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
            qs(arr, s, end)
        if start < e:
            qs(arr, start, e)


class Solution(object):
    def findContentChildren(self, g, s):
        index_g, index_s, res, size_g, size_s = 0, 0, 0, len(g), len(s)
        qs(g, 0, size_g-1)
        mg(s)
        while index_g < size_g and index_s < size_s:
            if g[index_g] <= s[index_s]:
                res += 1
                index_g += 1
            index_s += 1
        return res
