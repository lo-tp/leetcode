class Solution(object):
    def generateMatrix(self, n):
        res, size, index, h, v = [
            [0 for i in xrange(0, n)]for k in xrange(0, n)], n*n, 0, 0, 0
        start, end = 0, n-1
        h_offset, v_offset, offset_index = [1, 0, -1, 0], [0, 1, 0, -1], 0
        while index < size:
            next_h, next_v = h+h_offset[offset_index], v+v_offset[offset_index]
            if next_h < start or next_h > end or next_v < start or next_v > end:
                if offset_index == 3:
                    offset_index = 0
                    h, v = h+1, v+1
                    start += 1
                    end -= 1
                else:
                    offset_index += 1
                next_h, next_v = h + \
                    h_offset[offset_index], v+v_offset[offset_index]
            index += 1
            res[v][h] = index
            v, h = next_v, next_h
        return res


