class Solution(object):
    def spiralOrder(self, matrix):
        res, v_size = [], len(matrix)
        if v_size:
            h_offset, v_offset, h_size = [
                1, 0, -1, 0], [0, 1, 0, -1], len(matrix[0])
            index, size, h_start, h_end, v_start, v_end = 0, h_size * \
                v_size, 0, h_size-1, 0, v_size-1
            offset_index, v_index, h_index = 0, 0, 0
            while index < size:
                res.append(matrix[v_index][h_index])
                next_v, next_h = v_index + \
                    v_offset[offset_index], h_index+h_offset[offset_index]
                if next_v >= v_start and next_v <= v_end and next_h >= h_start and next_h <= h_end:
                    v_index, h_index = next_v, next_h
                else:
                    if offset_index == 3:
                        offset_index = 0
                        index -= 1
                        res.pop()
                        h_index += 1
                        v_index += 1
                        v_start += 1
                        v_end -= 1
                        h_start += 1
                        h_end -= 1
                    else:
                        offset_index += 1
                        v_index, h_index = v_index + \
                            v_offset[offset_index], h_index + \
                            h_offset[offset_index]
                index += 1
        return res
