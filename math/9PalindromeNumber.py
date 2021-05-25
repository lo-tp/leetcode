class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = '{}'.format(x)
        sz = len(string)
        for i in range(0, sz):
            if string[i] != string[sz-1-i]:
                return False
        return True
    def isPalindrome(self, x: int) -> bool:
        t = 0
        while x > t:
            residue = x % 10
            t = t*10+residue
            x = int((x-residue)/10)
        if x == t:
            return True
        return x == int(t/10)
    def isPalindrome(self, x: int) -> bool:
        if x and (not x % 10):
            return False
        t = 0
        while x > t:
            residue = x % 10
            t = t*10+residue
            x = int((x-residue)/10)
        return x==t or x == int(t/10)
