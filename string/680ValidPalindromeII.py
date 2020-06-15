class Solution(object):
    def validPalindrome(self, s):
        stack = [(0, len(s)-1, 1)]
        while stack:
            l, r, t = stack.pop()
            if l > r:
                return True
            if s[l] == s[r]:
                stack.append((l+1, r-1, t))
            if t:
                stack.append((l+1, r, 0))
                stack.append((l, r-1, 0))
        return False
