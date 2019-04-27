class Solution(object):
    def searchMatrix(self, matrix, target):
        column_size = len(matrix)
        if column_size:
            row_size = len(matrix[0])
            if row_size:
                for row in matrix:
                    s, e = 0, row_size-1
                    while s <= e:
                        m = s+(e-s)/2
                        if row[m] > target:
                            e = m-1
                        elif row[m] < target:
                            s = m+1
                        else:
                            return True
        return False

