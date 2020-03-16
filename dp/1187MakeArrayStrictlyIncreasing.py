from sys import maxint
from collections import defaultdict
from bisect import bisect_right


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
