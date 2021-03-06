class Solution(object):
    def largestRectangleAreaQuicker(self, heights):
        heights.append(0)
        res, s = 0, [(0, heights[0])]
        for i in xrange(1, len(heights)):
            if heights[i] > s[-1][1]:
                s.append((i, heights[i]))
            elif heights[i] < s[-1][1]:
                w = None
                while s and heights[i] < s[-1][1]:
                    w = s.pop()
                    res = max((i-w[0])*w[1], res)
                s.append((w[0], heights[i]))
        return res
    def largestRectangleArea(self, heights):
        heights.append(0)
        res, s = 0, [(0, heights[0])]
        for i in xrange(1, len(heights)):
            if heights[i] < s[-1][1]:
                w = None
                while s and s[-1][1] > heights[i]:
                    w = s.pop()
                    res = max(res, (i-w[0])*w[1])
                s.append((w[0], heights[i]))
            else:
                s.append((i, heights[i]))
        return res
