class Solution(object):
    def decodeString(self, s):
        res, stack = '', []
        for i in s:
            if i.isdigit():
                if stack and stack[-1][0] == 0:
                    stack[-1][1] = stack[-1][1]*10+int(i)
                else:
                    stack.append([0, int(i), ''])
            elif i == '[':
                stack[-1][0] = 1
            elif i == ']':
                status, number, str = stack.pop()
                tmp = ''.join([str]*number)
                if stack and stack[-1][0] == 1:
                    stack[-1][2] += tmp
                else:
                    res += tmp
            else:
                if stack and stack[-1][0] == 1:
                    stack[-1][2] += i
                else:
                    res += i
        return res
