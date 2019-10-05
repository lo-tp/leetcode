class Solution(object):
    def findNthDigit(self, n):
        tem, tmp = 9, 1
        while n > tem*tmp:
            n -= tem*tmp
            tem *= 10
            tmp += 1
        num = tem/9+n/tmp-1
        if n % tmp:
            num += 1
            residue = tmp-n % tmp
            while residue:
                residue-=1
                num/=10
        return num % 10

