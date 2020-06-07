class Solution(object):
    def palindromePairs(self, words):
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
