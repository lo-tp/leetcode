class Solution(object):
    def maxArea(self, height):
        res, sz, l = 0, len(height), 0
        r = sz-1
        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l]*(r-l))
                tmp = l+1
                while tmp < r and height[tmp] <= height[l]:
                    tmp += 1
                l = tmp
            else:
                res = max(res, height[r]*(r-l))
                tmp = r-1
                while tmp > l and height[tmp] <= height[r]:
                    tmp -= 1
                r = tmp
        return res
