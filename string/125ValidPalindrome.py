from re import sub


class Solution(object):
    def isPalindrome(self, s):
        t = sub('[^a-z0-9]', '', s.lower())
        sz = len(t)
        if sz > 1:
            m = sz/2
            return t[:m][::-1] == t[m+1 if sz % 2 else m:]
        return True

