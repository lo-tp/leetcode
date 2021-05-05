class Solution(object):
    def setZeroes(self, matrix):
        v_sz, h_sz = len(matrix), len(matrix[0])
        for v in range(0, v_sz):
            for h in range(0, h_sz):
                if matrix[v][h] == 0:
                    matrix[v][h] = None
                    for i in range(0, v_sz):
                        if matrix[i][h]:
                            matrix[i][h] = None
                    for i in range(0, h_sz):
                        if matrix[v][i]:
                            matrix[v][i] = None
        for v in range(0, v_sz):
            for h in range(0, h_sz):
                if not matrix[v][h]:
                    matrix[v][h] = 0
