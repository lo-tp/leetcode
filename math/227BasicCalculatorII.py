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
    def calculate(self, s):
        # remove spaces
        s = compile(' ').sub('', s)
        operator_reg = compile('^[+/*-]$')
        token, operator = [], []
        priorities = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 0,
        }
        for t in compile('[+/*-]|[()]|\d+').findall(s):
            if operator_reg.match(t):
                while operator and priorities[t] <= priorities[operator[-1]]:
                    token.append(operator.pop())
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

    def calculate(self, s):
        sz, re_num, re_operator = len(s), compile('\d'), compile('[+/*-]')
        stack, cur, operator = [('+', [])], 0, '+'
        for index in range(0, sz+1):
            if index == sz or re_operator.match(s[index]) or s[index] == ')':
                if operator == '*':
                    cur = stack[-1][1].pop()*cur
                elif operator == '/':
                    cur = int(stack[-1][1].pop()/cur)
                elif operator == '-':
                    cur *= -1
                stack[-1][1].append(cur)
                cur = 0
                if index != sz and s[index] == ')':
                    operator, t = stack.pop()
                    cur = sum(t)
                elif index != sz:
                    operator = s[index]
            elif s[index] == '(':
                stack.append((operator, []))
                operator = '+'
            elif re_num.match(s[index]):
                cur *= 10
                cur += ord(s[index])-ord('0')
        return sum(stack[-1][1])
