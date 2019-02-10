def calculateCoordinates(start, width):
    ret = []
    for i in xrange(0, width):
        ret.append([start[0]+i, start[1]+width])
        ret.append([start[0]+width, start[1]+i])
    ret.append([start[0]+width, start[1]+width])
    return ret


class Solution(object):
    def maximalSquareWithDP(self, matrix):
        res = 0
        if len(matrix):
            rowSz = len(matrix[0])
            if rowSz:
                dp = [0]*rowSz
                for row in matrix:
                    prev = 1 if row[0] == '1' else 0
                    for i in xrange(1, rowSz):
                        if row[i] == '1':
                            prev, dp[i-1] = min(dp[i-1], dp[i], prev)+1, prev
                        else:
                            prev, dp[i-1] = 0, prev
                    dp[-1] = prev
                    res = max(max(dp), res)
        return res*res

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
