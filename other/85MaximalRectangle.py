from sys import maxint


class Solution(object):
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
