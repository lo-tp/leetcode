class Solution(object):
    def orderlyQueue(self, S, K):
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

