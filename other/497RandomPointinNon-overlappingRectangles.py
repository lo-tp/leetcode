from typing import List
from math import floor
from random import randrange


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.outterIndex, self.index = randrange(0, len(rects)), 0
        self.data = [(x1, y2, x2 - x1, y2 - y1) for x1, y1, x2, y2 in rects]

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
