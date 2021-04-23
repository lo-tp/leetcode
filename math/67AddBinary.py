class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, sz_a, sz_b = False, len(a), len(b)
        if sz_a < sz_b:
            a, b, sz_a, sz_b = b, a, sz_b, sz_a
        b, a = list(b), list(a)
        for i in range(1, sz_b+1,):
            res = 1 if carry else 0
            if a[sz_a-i] == '1':
                res += 1
            if b[sz_b-i] == '1':
                res += 1
            a[sz_a-i] = '{}'.format(res % 2)
            carry = res > 1
        for i in range(sz_b+1, sz_a+1):
            res = 1 if carry else 0
            if a[sz_a-i] == '1':
                res += 1
            a[sz_a-i] = '{}'.format(res % 2)
            carry = res > 1
        a = ''.join(a)
        return '{}{}'.format(1, a) if carry else a

    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            carry, answer = (x & y) << 1, x ^ y
            x, y = answer, carry
        return bin(x)[2:]
