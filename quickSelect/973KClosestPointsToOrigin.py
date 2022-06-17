from typing import List, Tuple
from random import randrange
from math import ceil, floor


def shuffle(arr: Tuple[int, List[List[int]]]):
    sz = len(arr)
    for i in range(0, sz):
        j = randrange(i, sz)
        arr[i], arr[j] = arr[j], arr[i]


def partition(arr: Tuple[int, List[List[int]]], left: int, right: int):
    if left >= right:
        return right

    i, j, m = left, right + 1, arr[left][0]
    while True:
        while True:
            i += 1
            if arr[i][0] >= m or i == right:
                break
        while True:
            j -= 1
            if arr[j][0] <= m or j == left:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tmp: Tuple[int, List[List[int]]] = [
            (l[0] * l[0] + l[1] * l[1], l) for l in points
        ]
        left, right = 0, len(tmp) - 1
        k -= 1
        while True:
            j = partition(tmp, left, right)
            if j < k:
                left = j + 1
            elif j > k:
                right = j - 1
            else:
                break
        return [l[1] for l in tmp[:k+1]]
