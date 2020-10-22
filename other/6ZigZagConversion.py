class Solution(object):
    def convert(self, s, numRows):
        sz, res, index, row_index = len(
            s), [[] for _ in range(0, numRows)], 0, 0
        while index < sz:
            while index < sz and row_index < numRows:
                res[row_index].append(s[index])
                index += 1
                row_index += 1
            row_index -= 2
            while index < sz and row_index > 0:
                res[row_index].append(s[index])
                index += 1
                row_index -= 1
        return ''.join([''.join(row) for row in res])
