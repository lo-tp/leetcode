def calculateCoordinates(start, width):
    ret = []
    for i in xrange(0, width):
        ret.append([start[0]+i, start[1]+width])
        ret.append([start[0]+width, start[1]+i])
    ret.append([start[0]+width, start[1]+width])
    return ret


class Solution(object):
    def maximalSquareBF(self, matrix):
        res = 0
        vWidth = len(matrix)
        if vWidth:
            hWidth = len(matrix[0])
            for vIndex in xrange(0, vWidth):
                for hIndex in xrange(0, hWidth):
                    maxWidth = min(vWidth-vIndex, hWidth-hIndex)
                    if maxWidth > res:
                        tmp = 0
                        index = 0
                        while index < maxWidth:
                            if reduce(lambda accu, coos: accu and matrix[coos[0]][coos[1]] == '1',
                                      calculateCoordinates([vIndex, hIndex], index), True):
                                tmp += 1
                            else:
                                break
                            index += 1
                        res = max(tmp, res)
        return res**2
