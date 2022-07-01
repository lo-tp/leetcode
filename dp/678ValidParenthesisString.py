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

