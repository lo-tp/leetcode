class Solution(object):
    def flipAndInvertImage(self, A):
        v_sz = len(A)
        if v_sz:
            h_sz = len(A[0])
            for row in A:
                l, r = 0, h_sz-1
                while l < r:
                    row[l], row[r] = row[r], row[l]
                    row[l] ^= 1
                    row[r] ^= 1
                    r -= 1
                    l += 1
                if l == r:
                    row[r] ^= 1
        return A
