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
