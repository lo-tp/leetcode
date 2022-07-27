from typing import List, Optional

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for v in range(row1, row2 + 1):
            for h in range(col1, col2 + 1):
                res += self.matrix[v][h]
        return res
