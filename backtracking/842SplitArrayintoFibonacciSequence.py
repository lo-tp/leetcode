from typing import List


def isValidString(num: str):
    return not (len(num) > 1 and num[0] == "0")


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        sz, res = len(num), []
        for len1 in range(1, min(sz, 10)):
            for len2 in range(1, min(sz - len1, 10)):
                num1Str, num2Str = num[:len1], num[len1 : len1 + len2]
                if isValidString(num1Str) and isValidString(num2Str):
                    num1, num2 = int(num1Str), int(num2Str)
                    index = len1 + len2
                    potentialAnswer = [num1Str, num2Str]
                    isCorrect = True
                    while True:
                        num3 = num1 + num2
                        num3Str = str(num3)
                        len3 = len(num3Str)
                        nextIndex = index + len3
                        if nextIndex > sz:
                            isCorrect = False
                            break
                        nextStr = num[index:nextIndex]
                        if isValidString(nextStr) and nextStr == num3Str:
                            potentialAnswer.append(num3)
                            num1, num2 = num2, num3
                            if nextIndex == sz:
                                return potentialAnswer
                            index = nextIndex
                        else:
                            isCorrect = False
                            break
        return []

