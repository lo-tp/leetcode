from typing import List
from random import randrange


def heapify(arr, i, sz):
    stack = [i]
    while stack:
        t = max_i = stack.pop()
        r, l = t*2+2, t*2+1
        if r < sz and arr[r][0] > arr[max_i][0]:
            max_i = r
        if l < sz and arr[l][0] > arr[max_i][0]:
            max_i = l
        if max_i != t:
            arr[max_i], arr[t] = arr[t], arr[max_i]
            stack.append(max_i)


def heapSort(arr):
    sz = len(arr)
    for i in range(int((sz-2)/2), -1, -1):
        heapify(arr, i, sz)

    for i in range(sz-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    return arr


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        heapSort(clips)
        te = t = 0
        count = 1
        for start, end in clips:
            # print(start, end)
            # print(count, t, te, time)
            if t >= time:
                return count
            if start <= t:
                te = max(end, te)
            elif start <= te:
                t = te
                te = max(end, te)
                count += 1
            else:
                break
        return count if te >= time else -1

    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        heapSort(clips)
        te = t = 0
        count = 1
        for start, end in clips:
            # print(t, te, start, end, count)
            if t >= time:
                return count
            if not start:
                t = end
            else:
                if start <= t:
                    te = max(end, te)
                elif start <= te:
                    t = te
                    te = max(end, te)
                    count += 1
                else:
                    return -1
        return count if t >= time else (count+1 if te >= time else -1)
