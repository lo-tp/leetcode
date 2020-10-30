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
    def numMatchingSubseq(self, S, words):
        data, res, ord_a = [[] for _ in xrange(0, 26)], 0, ord('a')
        for w in words:
            data[ord(w[0])-ord_a].append(w)
        for i in S:
            t = ord(i)-ord_a
            for _ in xrange(0, len(data[t])):
                w = data[t].pop(0)
                if len(w) == 1:
                    res += 1
                else:
                    data[ord(w[1])-ord_a].append(w[1:])
        return res
