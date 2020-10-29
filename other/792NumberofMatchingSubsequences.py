from collections import Counter


class Solution(object):
    def numMatchingSubseq(self, S, words):
        res, sz = 0, len(S)
        for w in words:
            i, j, w_sz = 0, 0, len(w)
            while i < sz and j < w_sz:
                if S[i] == w[j]:
                    j += 1
                i += 1
            res += 1 if j == w_sz else 0
        return res
