from typing import List
from random import randrange
from math import ceil, floor


def shuffle(arr: List[int]):
    sz = len(arr)
    for i in range(0, sz):
        j = randrange(i, sz)
        arr[i], arr[j] = arr[j], arr[i]


def partition(arr: List[int], left: int, right: int):
    if left >= right:
        return right

    i, j, m = left, right + 1, arr[left]
    while True:
        while True:
            i += 1
            if arr[i] >= m or i == right:
                break
        while True:
            j -= 1
            if arr[j] <= m or j == left:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def qc(arr: List[int], left: int, right: int):
    if left < right:
        j = partition(arr, left, right)
        qc(arr, left, j - 1)
        qc(arr, j + 1, right)
    return arr


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        shuffle(nums)
        qc(nums, 0, len(nums) - 1)
        t = floor(len(nums) / 2)
        w = ceil(len(nums) / 2)
        index, tmp = 0, nums[:]
        for i in range(0, t):
            nums[index] = tmp[w - 1 - i]
            index += 1
            nums[index] = tmp[-1 - i]
            index += 1
        if len(nums) % 2:
