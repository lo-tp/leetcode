from re import compile

def addStrings(a: str, b: str) -> str:
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


class Solution(object):
    def multiply(self, num1, num2):
        res = '0'
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        ord_0, sz1, sz2 = ord('0'), len(num1), len(num2)
        t = ['0']*(sz2+1)
        for i in range(sz1-1, -1, -1):
            carry, te = 0, ord(num1[i])-ord_0
            for j in range(1, sz2+1, 1):
                tem = ord(num2[-j])-ord_0
                tem = tem*te+carry
                t[-j] = str(tem % 10)
                carry = int(tem/10)
            t[0] = str(carry)
            if(carry):
                res = addStrings(res, '{}{}'.format(''.join(t), '0'*(sz1-1-i)))
            else:
                res = addStrings(res, '{}{}'.format(
                    ''.join(t[1:]), '0'*(sz1-1-i)))
        return '0' if reg_0.match(res) else res
