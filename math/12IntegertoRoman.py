class Solution(object):
    def intToRoman(self, num):
        res = []
        while num:
            if num >= 1000:
                res.append('M')
                num -= 1000
            elif num >= 900:
                res.append('CM')
                num -= 900
            elif num >= 500:
                res.append('D')
                num -= 500
            elif num >= 400:
                res.append('CD')
                num -= 400
            elif num >= 100:
                res.append('C')
                num -= 100
            elif num >= 90:
                res.append('XC')
                num -= 90
            elif num >= 50:
                res.append('L')
                num -= 50
            elif num >= 40:
                res.append('XL')
                num -= 40
            elif num >= 10:
                res.append('X')
                num -= 10
            elif num >= 9:
                res.append('IX')
                num -= 9
            elif num >= 5:
                res.append('V')
                num -= 5
            elif num >= 4:
                res.append('IV')
                num -= 4
            else:
                res.append('I')
                num -= 1
        return ''.join(res)
