class Solution(object):
    def isToeplitzMatrix(self, matrix):
        v_size = len(matrix)
        if v_size:
            h_size = len(matrix[0])
            for v_start in xrange(0, v_size):
                val, v, h = matrix[v_start][0], v_start, 0
                while v < v_size and h < h_size:
                    if val != matrix[v][h]:
                        return False
                    v += 1
                    h += 1
            for h_start in xrange(0, h_size):
                val, v, h = matrix[0][h_start], 0, h_start
                while v < v_size and h < h_size:
                    if val != matrix[v][h]:
                        return False
                    v += 1
                    h += 1
        return True
