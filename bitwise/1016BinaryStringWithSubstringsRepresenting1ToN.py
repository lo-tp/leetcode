class Solution(object):
    def queryString(self, S, N):
        if N >= 2048:
            return False
        seen, t, te = set(), N.bit_length(), len(S)
        if t <= te:
            for i in xrange(1, t+1):
                k, tem, temp = 0, 0, 2**(i-1)
                for j in xrange(0, i-1):
                    tem *= 2
                    if S[j] == '1':
                        tem += 1
                for j in xrange(i-1, te):
                    tem *= 2
                    if S[j] == '1':
                        tem += 1
                    if tem and tem <= N:
                        seen.add(tem)
                    if S[k] == '1':
                        tem -= temp
                    k += 1
        return len(seen) == N

    def queryString(self, S, N):
        if N >= 2048:
            return False
        dp, seen, sz_s = [(0, i) for i in xrange(0, len(S))], set(),  len(S)
        for _ in xrange(0, N.bit_length()):
            tmp = []
            for cur, j in dp:
                if j < sz_s:
                    cur *= 2
                    cur += 1 if S[j] == '1' else 0
                    if cur and cur <= N:
                        seen.add(cur)
                    tmp.append((cur, j+1))
            dp = tmp
        return len(seen) == N
