def getTable(string):
    k, sz, table = -1, len(string), [-1 for _ in string]
    for i in xrange(1, sz):
        while k != -1 and string[k+1] != string[i]:
            k = table[k]
        if string[k+1] == string[i]:
            k += 1
        table[i] = k
    return table
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
    def shortestPalindromeWA(self, S):
        maximum, rev, table, sz, k = 0, S[::-1], getTable(S), len(S), -1
        print table
        for i in xrange(0, sz):
            while k != -1 and S[k+1] != rev[i]:
                # print k, i
                k = table[k]
            if S[k+1] == rev[i]:
                k += 1
            maximum = max(maximum, k)
        return '{}{}'.format(S[maximum+1:][::-1], S)

    def shortestPalindrome(self, S):
        maximum, rev, table, sz, k = 0, S[::-1], getTable(S), len(S), -1
        for i in xrange(0, sz):
            while k != -1 and S[k+1] != rev[i]:
                # print k, i
                k = table[k]
            if S[k+1] == rev[i]:
                k += 1
            maximum = max(maximum, k)
        return '{}{}'.format(rev[:sz-k-1], S)
