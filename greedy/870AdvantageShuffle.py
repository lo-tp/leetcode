from random import randrange

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


def reorder(arr):
    sz = len(arr)
    for i in range(0, sz):
        j = randrange(i, sz)
        arr[i], arr[j] = arr[j], arr[i]


def partition(arr, lo, hi):
    if lo == hi:
        return lo

    i, j, m = lo, hi+1, arr[lo]
    while True:
        while True:
            i += 1
            if i >= hi or arr[i][1] >= m[1]:
                break
        while True:
            j -= 1
            if j <= lo or arr[j][1] <= m[1]:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[lo] = arr[lo], arr[j]
    return j


def quick(arr, lo, hi):
    if hi > lo:
        j = partition(arr, lo, hi)
        quick(arr, lo, j-1)
        quick(arr, j+1, hi)


def qc(arr):
    sz = len(arr)
    reorder(arr)
    quick(arr, 0, sz-1)
    return arr



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

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1, arr2 = qc([(i, t) for i, t in enumerate(nums1)]), qc([(i, t)
                                                                    for i, t in enumerate(nums2)])
        l, r = 0, len(nums1)-1
        for _, t in arr1:
            if t > arr2[l][1]:
                nums1[arr2[l][0]] = t
                l += 1
            else:
                nums1[arr2[r][0]] = t
                r -= 1
        return nums1
