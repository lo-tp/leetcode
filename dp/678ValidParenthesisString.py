class Solution:
    def checkValidString(self, s: str) -> bool:
        sz = len(s)
        stack = [(0, 0)]
        while stack:
            lNum, index = stack.pop()
            if index == sz:
                if lNum:
                    break
                else:
                    return True
            if s[index] == "*":
                index += 1
                stack.append((lNum + 1, index))
                stack.append((lNum, index))
                if lNum:
                    stack.append((lNum - 1, index))
            elif s[index] == "(":
                index += 1
                stack.append((lNum + 1, index))
            elif lNum:
                index += 1
                stack.append((lNum - 1, index))
        return False

    def checkValidString(self, s: str) -> bool:
        leftBalance = rightBalance = 0
        sz = len(s)
        for i in range(0, sz):
            if s[i] == ")":
                leftBalance -= 1
            else:
                leftBalance += 1
            if leftBalance < 0:
                return False
            reversedIndex = sz - 1 - i
            if s[reversedIndex] == "(":
                rightBalance -= 1
            else:
                rightBalance += 1
            if rightBalance < 0:
                return False
        return True

