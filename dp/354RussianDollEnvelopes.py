from random import randrange

def partition(arr, lo, hi):
    if lo == hi:
        return lo
    i, j, m = lo, hi+1, arr[lo]
    while True:
        while True:
            i += 1
            if i == hi or arr[i][0] > m[0] or (arr[i][0] == m[0] and arr[i][1] <= m[1]):
                break
        while True:
            j -= 1
            if j == lo or arr[j][0] < m[0] or (arr[j][0] == m[0] and arr[j][1] >= m[1]):
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[lo] = arr[lo], arr[j]
    return j


def qc(arr, lo, hi):
    if hi > lo:
        m = partition(arr, lo, hi)
        qc(arr, lo, m-1)
        qc(arr, m+1, hi)


class Solution(object):
    def maxEnvelopes(self, envelopes):
        sz = len(envelopes)
        qc(envelopes, 0, sz-1)
        res, dp = 0, []
        for _, height in envelopes:
            l, r = 0, res-1
            while l <= r:
                m = int(l+(r-l)/2)
                if height < dp[m]:
                    r = m-1
                elif height > dp[m]:
                    l = m+1
                else:
                    r = m-1
            if l == res:
                dp.append(height)
                res += 1
            else:
                dp[l] = height
        return res

    def maxEnvelopes(self, envelopes):
        shuffle(envelopes)
        sz = len(envelopes)
        qc(envelopes, 0, sz-1)
        count, data = 0, [None]*sz
        for _, j in envelopes:
            l, r = 0, count-1
            while l <= r:
                m = int(l+(r-l)/2)
                if j < data[m]:
                    r = m-1
                elif j > data[m]:
                    l = m+1
                else:
                    r = m-1
            data[l] = j
            if l == count:
                count += 1
        # print(data)
        # print(envelopes)
        return count



def shuffle(arr):
    sz = len(arr)
    for i in range(0, sz):
        t = randrange(i, sz)
        arr[i], arr[t] = arr[t], arr[i]


def partition(arr, lo, hi):
    if lo == hi:
        return lo
    i, j, m = lo, hi+1, arr[lo]
    while True:
        while True:
            i += 1
            if i == hi or arr[i][0] > m[0] or (arr[i][0] == m[0] and arr[i][1] < m[1]):
                break
        while True:
            j -= 1
            if j == lo or arr[j][0] < m[0] or (arr[j][0] == m[0] and arr[j][1] > m[1]):
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[lo] = arr[lo], arr[j]
    return j


def qc(arr, lo, hi):
    if lo < hi:
        m = partition(arr, lo, hi)
        qc(arr, lo, m-1)
        qc(arr, m+1, hi)


