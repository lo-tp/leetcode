class Solution(object):
    def breakPalindrome(self, palindrome):
        sz = len(palindrome)
        if sz == 1:
            return ''
        t = list(palindrome)
        te = sz/2
        for i in xrange(0, te):
            if t[i] != 'a':
                break
        if t[i] != 'a':
            t[i] = 'a'
        else:
            t[-1] = 'b'
        return ''.join(t)
