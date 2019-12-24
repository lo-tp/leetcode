def getTable(S):
    table, sz = [-1 for _ in S], len(S)
    k = -1
    for i in xrange(1, sz):
        while k > -1 and S[k+1] != S[i]:
            k = table[k]
        if S[k+1] == S[i]:
            k += 1
        table[i] = k
    return table
class Solution(object):
    def repeatedStringMatch(self, A, B):
        table = getTable(B)
        a_sz, b_sz, i, k = len(A), len(B), 0, -1
        while i-k-1 < a_sz:
            j = i % a_sz
            while k > -1 and B[k+1] != A[j]:
                k = table[k]
            i += 1
            if B[k+1] == A[j]:
                k += 1
            if k == b_sz-1:
                return i/a_sz+(1 if i % a_sz else 0)
        return -1

    def repeatedStringMatchTLE(self, A, B):
        res, start_index, size_a, size_b = 1, 0, len(A), len(B)
        while start_index < size_a:
            i, j = start_index, 0
            while j < size_b and A[i] == B[j]:
                i += 1
                j += 1
                if i == size_a and j < size_b:
                    i = 0
                    res += 1
            if j == size_b:
                return res
            res = 1
            start_index += 1
        return -1

