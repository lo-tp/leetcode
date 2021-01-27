from re import compile


class Solution(object):
    def calculate(self, s):
        # remove spaces
        s = compile(' ').sub('', s)
        token, operator = [], []
        for t in compile('[+/*-]|[()]|\d+').findall(s):
            if t == '-' or t == '+':
                while operator and (operator[-1] == '*' or operator[-1] == '/'):
                    token.append(operator.pop())
                operator.append(t)
            elif t == '/' or t == '*':
                operator.append(t)
            elif t == '(':
                operator.append('(')
            elif t == ')':
                while operator[-1] != '(':
                    token.append(operator.pop())
                operator.pop()
            else:
                token.append(t)
        token.extend(operator[::-1])
        stack = []
        num_reg = compile('\d+')
        for t in token:
            if num_reg.match(t):
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                if t == '-':
                    stack.append(l-r)
                if t == '+':
                    stack.append(l+r)
                elif t == '*':
                    stack.append(l*r)
                elif t == '/':
                    stack.append(int(l/r))
        return stack[0]
