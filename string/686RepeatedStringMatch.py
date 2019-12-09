class Solution(object):
    def repeatedStringMatch(self, A, B):
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
