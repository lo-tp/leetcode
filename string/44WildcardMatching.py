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

