from re import sub
class Solution(object):
    def isMatch(self, s, p):
        sz, sz_s = len(p), len(s)
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            if j == sz and i == sz_s:
                return True
            if i == sz_s or j == sz:
                continue
            if p[j] == '*':
                stack.append((i, j+1))
                stack.append((i+1, j))
                stack.append((i+1, j+1))
            if p[j] == '?' or s[i] == p[j]:
                stack.append((i+1, j+1))
        return False


class Solution(object):
    def isMatch(self, s, p):
        p = sub('\*+', '*', p)
        sz, sz_s = len(p), len(s)
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            if j == sz and i == sz_s:
                return True
            if j == sz:
                continue
            if p[j] == '*':
                t, te = i+1, j+1
                stack.append((i, te))
                if i != sz_s:
                    stack.append((t, j))
                    if (t == sz_s and te == sz)or(t != sz_s and te != sz and s[t] == p[te]):
                        stack.append((t, te))
            if i == sz_s:
                continue
            elif p[j] == '?' or s[i] == p[j]:
                stack.append((i+1, j+1))
        return False

    def isMatch(self, s, p):
        t, dp, sz_s, sz_p = True, [True], len(s), len(p)
        for i in xrange(0, sz_p):
            if p[i] != '*':
                t = False
            dp.append(t)
        for i in xrange(0, sz_s):
            tmp = [p != '' and p[0] == '*']
            for j in xrange(1,  sz_p+1):
                if p[j-1] == '?':
                    tmp.append(dp[j-1])
                elif p[j-1] == '*':
                    tmp.append(dp[j] or tmp[-1])
                else:
                    tmp.append(s[i] == p[j-1] and dp[j-1])
            dp = tmp
        return dp[-1]

    def isMatch(self, s, p):
        t, dp, sz_p = True, [True], len(p)+1
        for i in p:
            if i != '*':
                t = False
            dp.append(t)
        tmp = dp[:]
        for i in s:
            tmp[0] = p != '' and p[0] == '*'
            for j in xrange(1, sz_p):
                if p[j-1] == '?':
                    tmp[j] = dp[j-1]
                elif p[j-1] == '*':
                    tmp[j] = dp[j] or tmp[j-1]
                else:
                    tmp[j] = p[j-1] == i and dp[j-1]
            tmp, dp = dp, tmp
        return dp[-1]
