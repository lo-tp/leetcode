import re


def convert(str):
    isNum, numerator, denominator = True, 0, 0
    for i in str:
        if i == '/':
            isNum = False
        elif isNum:
            numerator = numerator*10+int(i)
        else:
            denominator = denominator*10+int(i)
    return [numerator, denominator]


def gcd(a, b):
    if a < b:
        a, b = b, a
    residue = a % b
    if residue:
        return gcd(b, residue)
    return b



class Solution(object):
    def fractionAddition(self, expression):
        if expression:
            operators = re.split("[^+-]+", expression)
            if operators[0] != '':
                nums = [convert(i) for i in re.split("[+-]+", expression)[1:]]
                nums[0][0] *= -1
            else:
                nums = [convert(i) for i in re.split("[+-]+", expression)]
            operators = operators[1:-1]
            for index, i in enumerate(operators):
                if len(i) > 1:
                    nums[index+1][0] *= -1
            for index, i in enumerate(nums[1:]):
                if operators[index][0] == '+':
                    nums[0][0] = nums[0][0]*i[1]+i[0]*nums[0][1]
                else:
                    nums[0][0] = nums[0][0]*i[1]-i[0]*nums[0][1]
                nums[0][1] *= i[1]
                if nums[0][0]:
                    max_similarity = gcd(abs(nums[0][0]), nums[0][1])
                    nums[0][0] /= max_similarity
                    nums[0][1] /= max_similarity
                else:
                    nums[0][1] = 1
            return '{}/{}'.format(nums[0][0], nums[0][1])
        return ''



S = Solution()
