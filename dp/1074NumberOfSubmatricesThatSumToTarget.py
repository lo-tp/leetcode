def getMatrixStr(x1, y1, x2, y2):
    return '%d %d %d %d' % (x1, y1, x2, y2)


class Solution(object):
    def numSubmatrixSumTarget(self, A, target):
        res, column_size = 0, len(A)
        if column_size:
            row_size = len(A[0])
            if row_size:
                for row in A:
                    for i in xrange(0, row_size-1):
                        row[i+1] += row[i]

                for l in xrange(0, row_size):
                    for r in xrange(l, row_size):
                        data = defaultdict(lambda: 0)
                        data[0] = 1
                        current = 0
                        for k in xrange(0, column_size):
                            current += A[k][r] - \
                                (0 if l == 0 else A[k][l-1])
                            res += data[current-target]
                            data[current] += 1
        return res
    def numSubmatrixSumTargetTLE(self, matrix, target):
        data, res, column_size = {}, 0, len(matrix)
        if column_size:
            row_size = len(matrix[0])
            if row_size:
                for y in xrange(0, column_size):
                    for x in xrange(0, row_size):
                        data[getMatrixStr(x, y, x, y)] = matrix[y][x]
                        if matrix[y][x] == target:
                            res += 1
                        for a in xrange(0, x):
                            string = getMatrixStr(a, y, x, y)
                            data[string] = data[getMatrixStr(
                                a, y, x-1, y)]+matrix[y][x]
                            if data[string] == target:
                                res += 1
                        for b in xrange(0, y):
                            for a in xrange(0, x+1):
                                string = getMatrixStr(a, b, x, y)
                                data[string] = data[getMatrixStr(
                                    a, b, x, y-1)]+data[getMatrixStr(a, y, x, y)]
                                if data[string] == target:
                                    res += 1
        return res
