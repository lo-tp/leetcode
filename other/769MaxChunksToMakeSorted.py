class Solution(object):
    def maxChunksToSorted(self, arr):
        pos, res, t = arr[:], 0, -1
        for i, j in enumerate(arr):
            pos[j] = i
        for i, j in enumerate(pos):
            if i != j:
                t = max(t, j)
                if i == t:
                    res += 1
            elif i > t:
                res += 1
        return res

