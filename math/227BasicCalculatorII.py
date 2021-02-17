from re import compile

def calculate(args):
    input, operators, is_positive = args
    t = []
    input.extend(operators[::-1])
    for token in input:
        if type(token) == int:
            t.append(token)
        else:
            a, b = t.pop(), t.pop()
            if token == '-':
                t.append(b-a)
            elif token == '/':
                t.append(int(b/a))
            elif token == '+':
                t.append(a+b)
            else:
                t.append(a*b)
    return t[-1] if is_positive else -t[-1]



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
    def calculate(self, s: str) -> int:
        reg_operator, reg_to_sep = compile('[+*/-]'), compile('[+*/()-]|\d+')
        is_num_positive, is_prev_operator, stack = True, True, []
        priorities = {
            '+': 1,
            '-': 1,
            '/': 2,
            '*': 2
        }
        for token in reg_to_sep.findall('({}'.format(s)):
            if token == '(':
                stack.append(([], [], is_num_positive))
            elif token == ')':
                num = calculate(stack.pop())
                stack[-1][0].append(num)
                is_num_positive, is_prev_operator = True, False
            elif reg_operator.match(token):
                if is_prev_operator and (token == '-' or token == '+'):
                    is_num_positive = token == '+'
                else:
                    output, operators, _ = stack[-1]
                    while operators and priorities[token] <= priorities[operators[-1]]:
                        output.append(operators.pop())
                    operators.append(token)
                    is_prev_operator = True
            else:
                stack[-1][0].append(int(token))
                if not is_num_positive:
                    stack[-1][0][-1] *= -1
                    is_num_positive = True
                is_prev_operator = False
        return calculate(stack.pop())
