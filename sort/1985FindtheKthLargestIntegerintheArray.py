from typing import List
from random import randrange
from math import floor


def siftDown(arr: List[int], index: int, sz: int):
    stack = [index]
    while stack:
        t = i = stack.pop()
        l, r = 2 * t + 1, 2 * t + 2
        if l < sz and arr[l] < arr[t]:
            t = l
        if r < sz and arr[r] < arr[t]:
            t = r
        if t != i:
            arr[t], arr[i] = arr[i], arr[t]
            stack.append(t)


def heapify(arr: List[int]):
    sz = len(arr)
    t = floor((sz - 1) / 2)
    for i in range(t, -1, -1):
        siftDown(arr, i, sz)


def heapSort(arr):
    heapify(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        siftDown(arr, 0, i)
    return arr


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for i in range(0, k):
            heap.append(int(nums[i]))
        heapify(heap)

        for i in range(k, len(nums)):
            j=int(nums[i])
            if j > heap[0]:
                heap[0] = j
                siftDown(heap, 0, k)
        heapSort(heap)

        return str(heap[-1])
