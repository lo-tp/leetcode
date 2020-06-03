class Solution(object):
    def shortestPalindrome(self, s):
        sz = len(s)
        if sz > 1:
            res = '{}{}'.format(s[1:][::-1], s)
            for i in xrange(1, (sz+1)/2):
                flag = True
                for j in xrange(0, i):
                    if s[j] != s[2*i-j]:
                        flag = False
                        break
                if flag:
                    res = min(res, '{}{}'.format(s[2*i+1:][::-1], s), key=len)
            for i in xrange(1, sz/2+1):
                flag = True
                for j in xrange(0, i):
                    if s[j] != s[2*i-j-1]:
                        flag = False
                        break
                if flag:
                    res = min(res, '{}{}'.format(s[2*i:][::-1], s), key=len)

            return res
        return s
