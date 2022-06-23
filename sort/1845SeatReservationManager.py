from typing import List
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
    for i in range(floor((sz - 1) / 2), -1, -1):
        siftDown(arr, i, sz)


class Heap:
    def __init__(self, arr: List[int] = []):
        self.arr = arr
        self.sz = len(arr)

    def heapify(self):
        heapify(self.arr)

    def pop(self):
        self.sz -= 1
        self.arr[self.sz], self.arr[0] = self.arr[0], self.arr[self.sz]
        siftDown(self.arr, 0, self.sz)
        return self.arr[self.sz]

    def insert(self, t: int):
        self.arr[self.sz] = t
        self.sz += 1
        for i in range(floor((self.sz - 1) / 2), -1, -1):
            siftDown(self.arr, i, self.sz)


class SeatManagerTle:
    def __init__(self, n: int):
        self.heap = Heap([i for i in range(1, n + 1)])

    def reserve(self) -> int:
        return self.heap.pop()

    def unreserve(self, seatNumber: int) -> None:


class SeatManager:
    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)
