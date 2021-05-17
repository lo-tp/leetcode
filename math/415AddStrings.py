class Solution:
    def addStrings(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        ord_0, sz, carry = ord('0'), len(b), False
        res = ['']*(sz+1)
        for i in range(1, len(a)+1):
            c, d = ord(a[-i])-ord_0, ord(b[-i])-ord_0
            c += d
            if carry:
                c += 1
            if c > 9:
                carry = True
                c %= 10
            else:
                carry = False
            res[-i] = str(c)
        for i in range(len(a)+1, sz+1):
            c = ord(b[-i])-ord_0
            if carry:
                c += 1
            if c > 9:
                carry = True
                c %= 10
            else:
                carry = False
            res[-i] = str(c)
        if carry:
            res[0] = '1'
        return ''.join(res)
