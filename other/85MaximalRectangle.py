from sys import maxint


class Solution(object):
    def maximalRectangleBest(self, matrix):
        res, c_sz = 0, len(matrix)
        if c_sz:
            r_sz = len(matrix[0])
            if r_sz:
                dp = [0]*(c_sz+1)
                for row in xrange(0, r_sz):
                    for column in range(0, c_sz):
                        if matrix[column][row] == '1':
                            dp[column] += 1
                        else:
                            dp[column] = 0
                    stack = [(dp[0], -1)]
                    for index, height in enumerate(dp[1:]):
                        if stack and stack[-1][0] >= height:
                            prevIndex = None
                            while stack and stack[-1][0] >= height:
                                h, prevIndex = stack.pop()
                                res = max(res, (index-prevIndex)*h)
                            stack.append((height, prevIndex))
                        else:
                            stack.append((height, index))
        return res
    def maximalRectangleBetter(self, matrix):
        res, columnSz = 0, len(matrix)
        if columnSz:
            rowSz = len(matrix[0])
            if rowSz:
                data = [[0]*rowSz for i in xrange(0, columnSz)]
                for r in xrange(0, rowSz):
                    count = 0
                    for c in xrange(0, columnSz):
                        if matrix[c][r] == '1':
                            count += 1
                        else:
                            count = 0
                        data[c][r] = count
                for rowData in data:
                    rowData.append(0)
                    stack=[(rowData[0], -1)]
                    for index,height  in enumerate(rowData[1:]):
                        if stack and height<=stack[-1][0]:
                            prevIndex=None
                            while stack and height<=stack[-1][0]:
                                h,prevIndex=stack.pop()
                                res=max(res, h*(index-prevIndex))
                            stack.append((height, prevIndex))
                        else:
                            stack.append((height, index))
        return res
    def maximalRectangle(self, matrix):
        res, columnSz = 0, len(matrix)
        if columnSz:
            rowSz = len(matrix[0])
            if rowSz:
                data = [[0]*rowSz for i in xrange(0, columnSz)]
                for c in xrange(0, columnSz):
                    count = 0
                    for r in xrange(0, rowSz):
                        if matrix[c][r] == '1':
                            count += 1
                        else:
                            count = 0
                        data[c][r] = count
                for c in xrange(0, columnSz):
                    for r in xrange(0, rowSz):
                        height, minWidth, col = 0, maxint, c
                        while col < columnSz and data[col][r]:
                            minWidth = min(minWidth, data[col][r])
                            height += 1
                            res = max(res, minWidth*height)
                            col += 1
        return res
