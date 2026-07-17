from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Check all 4 possible rotations (0, 90, 180, 270 degrees)
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
            
        return False
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotates the matrix 90 degrees clockwise in-place."""
        sz = len(matrix)
        # Step 1: Transpose the matrix
        for v_idx in range(sz):
            for h_idx in range(v_idx + 1, sz):
                matrix[v_idx][h_idx], matrix[h_idx][v_idx] = matrix[h_idx][v_idx], matrix[v_idx][h_idx]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

