class Solution(object):
    def queryString(self, S, N):
        if N > 2000:
            return False
        seen, sz = set(), N.bit_length()
        for i in xrange(1, sz+1):
            t, tem, res = 0, 2**(i-1), 0
            for j in xrange(0, i-1):
                res *= 2
                if S[j] == '1':
                    res += 1
            for j in xrange(i-1, len(S)):
                res *= 2
                if S[j] == '1':
                    res += 1
                if res and res <= N:
                    seen.add(res)
                if S[t] == '1':
                    res -= tem
                t += 1
        return len(seen) == N
