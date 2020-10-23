class Solution(object):
    def myAtoi(self, s):
        sz, index, is_neg, res, ord_0 = len(s), 0, False, 0, ord('0')
        while index < sz and s[index] == ' ':
            index += 1
        if index < sz:
            if s[index] == '-':
                is_neg = True
                index += 1
            elif s[index] == '+':
                index += 1
            elif ord_0 > ord(s[index]) or ord_0+9 < ord(s[index]):
                return res
            for i in range(index, sz):
                ord_i = ord(s[i])
                if ord_0 <= ord_i <= ord_0+9:
                    res = res*10+ord_i-ord_0
                else:
                    break
        if is_neg:
            res *= -1
        if res < -(1 << 31):
            return -(1 << 31)
        elif res >= 1 << 31:
            return (1 << 31)-1
        return res
