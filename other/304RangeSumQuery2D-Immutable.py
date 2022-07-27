from typing import List, Optional


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        vSz, hSz = len(matrix), len(matrix[0])
        total = 0
        for h in range(0, hSz):
            total += matrix[0][h]
            matrix[0][h] = total
        for v in range(1, vSz):
            preV, total = v - 1, 0
            for h in range(0, hSz):
                total += matrix[v][h]
                matrix[v][h] = matrix[preV][h] + total
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not row1 and not col1:
            return self.matrix[row2][col2]
        elif not row1:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif not col1:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        else:
            return (
                self.matrix[row2][col2]
                - self.matrix[row1 - 1][col2]
                - self.matrix[row2][col1 - 1]
                + self.matrix[row1 - 1][col1 - 1]
            )

