class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif i == '[':
                stack.append(i)
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif i == '{':
                stack.append(i)
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return not stack
    def isValid(self, s):
        stack = []
        for i in s:
            if i == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif i == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif i == '}':
                if not stack or stack.pop() != '{':
                    return False
            else:
                stack.append(i)
        return not stack
