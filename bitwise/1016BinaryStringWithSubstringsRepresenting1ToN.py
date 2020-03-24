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
