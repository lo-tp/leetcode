def add(num1, num2):
    sz1, sz2 = len(num1), len(num2)
    if sz1 > sz2:
        sz1, sz2, num1, num2 = sz2, sz1, num2, num1
    ord_0, res, carry = ord('0'), ['']*(sz2+1), False
    for i in range(-1, -sz1-1, -1):
        a, b = ord(num1[i])-ord_0, ord(num2[i])-ord_0
        a += b
        if carry:
            a += 1
        carry = True if a > 9 else False
        res[i] = str(a % 10)
    for i in range(-sz1-1, -sz2-1, -1):
        a = ord(num2[i])-ord_0
        if carry:
            a += 1
        carry = True if a > 9 else False
        res[i] = str(a % 10)
    if carry:
        res[0] = '1'
    return ''.join(res)

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
            sz = len(num)
            if sz < 3:
                return False
            for length in range(1, 2 if num[0] == '0' else int((sz-1)/2)+1):
                initial_num = int(num[:length])
                for length_2 in range(1, 2 if num[length] == '0' else int((sz-length)/2)+1):
                    index = length+length_2
                    a, b = initial_num, int(num[length: index])
                    while True:
                        if index == sz:
                            return True
                        c = a+b
                        if c and num[index] == '0':
                            break
                        c_str = str(c)
                        end_index = index+len(c_str)
                        if end_index <= sz and c_str == num[index:end_index]:
                            index, a, b = end_index, b, c
                        else:
                            break
            return False

    def isAdditiveNumber(self, num: str) -> bool:
        sz = len(num)
        if sz>2:
            for first in ([1] if num[0] == '0' else [i for i in range(1, int((sz-1)/2)+1)]):
                for second in [1] if num[first] == '0' else [i for i in range(1, sz-first)]:
                    if sz-first-second >= max(first, second):
                        a, b, i = num[:first], num[first:first +
                                                   second], first+second
                        while i != sz:
                            c = add(a, b)
                            c_sz = len(c)
                            if i+c_sz > sz:
                                break
                            if num[i] == '0':
                                if c != '0':
                                    break
                            elif num[i:i+c_sz] != c:
                                break
                            a, b = b, c
                            i += c_sz
                        if i == sz:
                            return True
