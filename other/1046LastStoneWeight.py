from typing import List
from math import floor


def siftDown(arr: List[int], index: int, sz: int):
    stack = [index]
    while stack:
        i = t = stack.pop()
        l = t * 2 + 1
        r = l + 1
        if l < sz and arr[l] > arr[t]:
            t = l
        if r < sz and arr[r] > arr[t]:
            t = r
        if t != i:
            arr[t], arr[i] = arr[i], arr[t]
            stack.append(t)


def heapify(arr: List[int]):
    sz = len(arr)
    for i in range(floor((sz - 1) / 2), -1, -1):
        siftDown(arr, i, sz)


def pop(arr: List[int]):
    arr[0], arr[-1] = arr[-1], arr[0]
    res = arr.pop()
    siftDown(arr, 0, len(arr))
    return res


def push(arr: List[int], target: int):
    arr.append(target)
    sz = len(arr)
    index = floor((sz - 1) / 2)
    while index != -1:
        t = arr[index]
        siftDown(arr, index, sz)
        if t == arr[index]:
            index = -1
        else:
            index = floor((index - 1) / 2)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(stones)
        while len(stones) > 1:
            x, r = pop(stones), pop(stones)
            if x != r:
                push(stones, abs(x - r))
        return stones[0] if stones else 0
