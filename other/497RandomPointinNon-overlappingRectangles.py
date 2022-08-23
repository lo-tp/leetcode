from typing import List
from math import floor
from random import randrange
from functools import reduce


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.outterIndex, self.index = randrange(0, len(rects)), 0
        self.data = [(x1, y2, x2 - x1 + 1, y2 - y1 + 1) for x1, y1, x2, y2 in rects]

    def pick(self) -> List[int]:
        x, y, w, h = self.data[self.outterIndex]
        xOffset, yOffset = self.index % w, floor(self.index / w)
        self.index -= 1
        res = [x + xOffset, y - yOffset]
        if self.index == -1:
            self.outterIndex -= 1
            if self.outterIndex == -1:
                self.outterIndex = len(self.data) - 1
            x, y, w, h = self.data[self.outterIndex]
            self.index = w * h - 1
        return res


class SolutionWithRandom:
    def __init__(self, rects: List[List[int]]):
        accu = 0
        self.data = [(0, 0, 0, 0)]
        for x1, y1, x2, y2 in rects:
            accu += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.data.append((x1, y1, x2 - x1 + 1, accu))
            # print(accu)
        self.rectsSz = len(rects) + 1
        # print(self.data)

    def pick(self) -> List[int]:
        l, r, outterIndex = 1, self.rectsSz - 1, 1
        index = randrange(0, self.data[-1][3])
        while l <= r:
            m = floor((r - l) / 2) + l
            if index < self.data[m - 1][3]:
                r = m - 1
            elif index >= self.data[m][3]:
                l = m + 1
            else:
                outterIndex = m
                break
        # print(self.data[-1][3], index, outterIndex)
        # print(self.data)
        x, y, w, _ = self.data[outterIndex]
        index -= self.data[outterIndex - 1][3]
        # print(index)
        xOffset, yOffset = index % w, floor(index / w)
        res = [x + xOffset, y + yOffset]
        return res

