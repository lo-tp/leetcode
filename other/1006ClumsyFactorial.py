def help(start):
    flag, res, end = True, start, max(0, start-3)
    for i in xrange(start-1, end, -1):
        if flag:
            res *= i
            flag = not flag
        else:
            res /= i
    return (res, end)


class Solution(object):
    def clumsy(self, N):
        res, t = help(N)
        flag = True
        while t:
            if flag:
                res += t
                t -= 1
            else:
                te, t = help(t)
                res -= te
            flag = not flag
        return res

