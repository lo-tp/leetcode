class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            bit=n&-n
            res+=1
            n^=bit
        return res
