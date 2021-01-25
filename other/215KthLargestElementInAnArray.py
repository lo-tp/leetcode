from heapq import heappush, heappop, heapify
from random import randrange

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
            if arr[i] >= m or i == hi:
                break
        while True:
            j -= 1
            if arr[j] <= m or j == lo:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[lo] = arr[lo], arr[j]
    return j



def heapify(arr):
    size = len(arr)
    if size > 1:
        index = (size-2)/2
        while index >= 0:
            mIndex = index*2+1
            rightIndex = mIndex+1
            if rightIndex < size and arr[rightIndex] < arr[mIndex]:
                mIndex = rightIndex
            if mIndex < size and arr[mIndex] < arr[index]:
                arr[mIndex], arr[index] = arr[index], arr[mIndex]
            index -= 1


class Solution(object):
    def findKthLargest(self, nums, k):
        first = nums[:k]
        heapify(first)
        for i in nums[k:]:
            if i > first[0]:
                first[0] = i
                heapify(first)
        return first[0]


class Solution(object):
    def findKthLargest(self, nums, k):
        data = []
        k = len(nums)-k+1
        for i in range(0, k):
            data.append(-nums[i])
        heapify(data)
        for j in range(k, len(nums)):
            if -nums[j] > data[0]:
                heappop(data)
                heappush(data, -nums[j])
        return -data[0]
    def findKthLargest(self, nums, k):
        l, r = 0, len(nums)-1
        target = len(nums)-k
        shuffle(nums)
        while l <= r:
            t = partition(nums, l, r)
            if t == target:
                return nums[t]
            elif t < target:
                l = t+1
            else:
                r = t-1
        return -1
