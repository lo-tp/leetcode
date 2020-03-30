from collections import Counter
from re import sub


class Solution(object):
    def largestMultipleOfThree(self, digits):
        res, total = '', sum(digits)
        data, residue = Counter(digits), total % 3
        if residue == 2:
            if 2 in data:
                data[2] -= 1
                residue -= 2
            elif 5 in data:
                data[5] -= 1
                residue -= 2
            elif 8 in data:
                data[8] -= 1
                residue -= 2
            for i in xrange(0, residue):
                if 1 in data and data[1]:
                    data[1] -= 1
                    residue -= 1
                elif 4 in data and data[4]:
                    data[4] -= 1
                    resudue -= 1
                elif 7 in data and data[7]:
                    data[7] -= 1
                    residue -= 1
        elif residue == 1:
            if 1 in data and data[1]:
                data[1] -= 1
                residue -= 1
            elif 4 in data and data[4]:
                data[4] -= 1
                resudue -= 1
            elif 7 in data and data[7]:
                data[7] -= 1
                residue -= 1
            if residue:
                residue += 1
                for i in xrange(0, 2):
                    if 2 in data and data[2]:
                        data[2] -= 1
                        residue -= 1
                    elif 5 in data and data[5]:
                        data[5] -= 1
                        residue -= 1
                    elif 8 in data and data[8]:
                        data[8] -= 1
                        residue -= 1
        if not residue:
            t = [k for k in data.keys() if data[k]]
            t.sort()
            for i in t[::-1]:
                for j in xrange(0, data[i]):
                    res += str(i)
            res = sub('^0+', '0', res)
        return res

    def largestMultipleOfThree(self, digits):
        res, residue, data = '', sum(digits) % 3, Counter(digits)
        if residue == 2:
            for i in [i for i in [2, 5, 8] if i in data]:
                data[i] -= 1
                residue -= 2
                break
            if residue:
                for i in [i for i in [1, 4, 7] if i in data]:
                    if residue:
                        residue -= 1
                        data[i] -= 1
                    if residue and data[i]:
                        residue -= 1
                        data[i] -= 1
                    if not residue:
                        break
        elif residue:
            for i in [i for i in [1, 4, 7] if i in data]:
                data[i] -= 1
                residue -= 1
                break
            if residue:
                residue = 2
                for i in [i for i in [2, 5, 8] if i in data]:
                    if residue:
                        residue -= 1
                        data[i] -= 1
                    if residue and data[i]:
                        residue -= 1
                        data[i] -= 1
                    if not residue:
                        break
        if not residue:
            for i in [i for i in xrange(9, -1, -1) if i in data and data[i]]:
                res += str(i)*data[i]
        return sub('^0+', '0', res)

