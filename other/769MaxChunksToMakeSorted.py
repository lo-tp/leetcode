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

    def maxChunksToSortedBetter(self, arr):
        t, res = 0, 0
        for i, j in enumerate(arr):
            if i != j:
                t = max(j, t)
            if i >= t:
                res += 1
        return res
