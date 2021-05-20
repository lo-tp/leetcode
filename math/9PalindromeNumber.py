class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = '{}'.format(x)
        sz = len(string)
        for i in range(0, sz):
            if string[i] != string[sz-1-i]:
                return False
        return True
