def calculateCoordinates(start, width):
    ret = []
    for i in xrange(0, width):
        ret.append([start[0]+i, start[1]+width])
        ret.append([start[0]+width, start[1]+i])
    ret.append([start[0]+width, start[1]+width])
    return ret


class Solution(object):
    def maximalSquareWithDP(self, matrix):
        height, res = len(matrix), 0
        if height:
            width = len(matrix[0])
            dp = [0 if k == '0' else 1 for k in matrix[0]]
            res = max(dp+[res])
            for i in xrange(1, height):
                prev = 1 if matrix[i][0] == '1' else 0
                for j in xrange(1, width):
                    if matrix[i][j] == '1':
                        dp[j-1], prev = prev, min(dp[j], dp[j-1], prev)+1
                    else:
                        dp[j-1], prev = prev, 0

                dp[width-1] = prev
                res = max(dp+[res])
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
