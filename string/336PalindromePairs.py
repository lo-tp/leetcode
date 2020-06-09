def isPalindrome(s):
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution(object):
    def palindromePairsTLE(self, words):
        res, sz = [], len(words)
        for i in xrange(0, sz):
            for j in xrange(i+1, sz):
                for t, te in [(i, j), (j, i)]:
                    s = '{}{}'.format(words[t], words[te])
                    flag, l, r = True, 0, len(s)-1
                    while l <= r:
                        if s[l] != s[r]:
                            flag = False
                            break
                        l += 1
                        r -= 1
                    if flag:
                        res.append([t, te])
        return res
    def palindromePairs(self, words):
        res, data = [], {}
        for i, t in enumerate(words):
            data[t[::-1]] = i
        for index, w in enumerate(words):
            for i in xrange(0, len(w)):
                l, r = w[:i], w[i:]
                if l in data and data[l] != index and isPalindrome(r):
                    res.append([index, data[l]])
                    if not l:
                        res.append([data[l], index])
                if r in data and data[r] != index and isPalindrome(l):
                    res.append([data[r], index])
        return res
