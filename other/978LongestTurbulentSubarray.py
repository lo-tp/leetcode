class Solution(object):
    def maxTurbulenceSize(self, A):
        s, sz, res = 0, len(A), 1 if A else 0
        while s+1 < sz:
            while s+1 < sz and A[s] == A[s+1]:
                s += 1
            if s+1 < sz:
                e = s+1
                flag = A[s] < A[e]
                while e+1 < sz:
                    if flag and A[e] <= A[e+1]:
                        break
                    elif (not flag) and A[e] >= A[e+1]:
                        break
                    e += 1
                    flag = not flag
                res = max(res, (e-s)+1)
                s = e
        return res
