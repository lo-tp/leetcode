from sys import maxint
from collections import defaultdict
from bisect import bisect_right
from sys import maxsize


def mergeSort(arr):
    sz = len(arr)
    if sz > 1:
        l_index, r_index, index, m = 0, 0, 0, sz/2
        l, r = arr[:m], arr[m:]
        l_sz, r_sz = len(l), len(r)
        mergeSort(l)
        mergeSort(r)
        while l_index < l_sz and r_index < r_sz:
            if l[l_index] < r[r_index]:
                arr[index] = l[l_index]
                l_index += 1
            else:
                arr[index] = r[r_index]
                r_index += 1
            index += 1
        while r_index < r_sz:
            arr[index] = r[r_index]
            r_index += 1
            index += 1
        while l_index < l_sz:
            arr[index] = l[l_index]
            l_index += 1
            index += 1

def shuffle(arr):
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
            if i == hi or arr[i] >= m:
                break
        while True:
            j -= 1
            if j == lo or arr[j] <= m:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    return j


def qc(arr, lo, hi):
    if hi > lo:
        j = partition(arr, lo, hi)
        qc(arr, lo, j-1)
        qc(arr, j+1, hi)



class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        mergeSort(arr2)
        sz_2, dp = len(arr2), {-1: 0}
        for i in arr1:
            tmp = defaultdict(lambda: maxint)
            for j in dp:
                if i > j:
                    tmp[i] = min(tmp[i], dp[j])
                t = bisect_right(arr2, j)
                if t < sz_2:
                    tmp[arr2[t]] = min(tmp[arr2[t]], dp[j]+1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        sz, dp = len(arr2), {-maxint: 0}
        for i in arr1:
            tmp = defaultdict(lambda: max)
            for key, val in dp.items():
                if i > key:
                    tmp[i] = min(val, tmp[i])
                t = bisect_right(arr2, key)
                if t < sz:
                    tmp[arr2[t]] = min(val+1, tmp[arr2[t]])
            dp = tmp
        return min(dp.values()) if dp else -1
    def makeArrayIncreasing(self, arr1, arr2):
        sz2 = len(arr2)
        qc(arr2, 0, sz2-1)
        data = {-1: 0}
        for i in arr1:
            tmp = defaultdict(lambda: maxsize)
            for key, val in data.items():
                if i > key:
                    tmp[i] = min(tmp[i], val)
                j = bisect_right(arr2, key)
                if j != sz2:
                    tmp[arr2[j]] = min(tmp[arr2[j]], val+1)
            data = tmp
        return min(data.values()) if data else -1
