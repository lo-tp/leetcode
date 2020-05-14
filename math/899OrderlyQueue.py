class Solution(object):
    def orderlyQueueTLE(self, S, K):
        seen, stack, res = set(), [S], S
        while stack:
            s = stack.pop()
            if s in seen:
                continue
            seen.add(s)
            if s < res:
                res = s
            for i in xrange(0, K):
                t, te = s[:i], s[i+1:]
                stack.append('{}{}{}'.format(t, te, s[i]))
        return res

    def orderlyQueue(self, S, K):
        res = S
        if K > 1:
            w = [ord(i) for i in S]
            w.sort()
            res = ''.join([chr(i) for i in w])
        else:
            sz = len(S)
            t = S
            for i in xrange(0, sz):
                t = '{}{}'.format(t[1:], t[0])
                res = min(res, t)
        return res

    def orderlyQueue(self, S, K):
        return ''.join([chr(i) for i in sorted([ord(j) for j in S])]) if K-1 else min(['{}{}'.format(S[i:], S[:i]) for i in xrange(0, len(S))])

