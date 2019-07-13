def qc(arr, start, end):
    s, e, m = start, end, arr[start+(end-start)/2][0]
    while s <= e:
        while arr[s][0] < m:
            s += 1
        while arr[e][0] > m:
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
    def advantageCount(self, A, B):
        arr_a, arr_b, res = [[i, index] for index, i in enumerate(
            A)], [[i, index] for index, i in enumerate(B)], A
        if arr_a:
            qc(arr_a, 0, len(A)-1)
            qc(arr_b, 0, len(A)-1)
            index = 0
            tmp, dropped = [], []
            for ele in arr_a:
                i, _ = ele
                if i > arr_b[index][0]:
                    tmp.append(ele)
                    index += 1
                else:
                    dropped.append(ele)
            tmp.extend(dropped)
            for index, ele in enumerate(arr_b):
                _, i = ele
                res[i] = tmp[index][0]
        return res
