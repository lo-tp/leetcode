import re;

regToSep = re.compile('[+/*()-]|\d+')
regOperator = re.compile('^[+/*-]$')
reNum = re.compile('\d+')

priorities={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '(':0,
}

def toRPN(input):
    operators=[]
    output=[]
    tokens=regToSep.findall(input)
    for t in tokens:
        if reNum.match(t):
            output.append(t)
        elif regOperator.match(t):
            while len(operators) and priorities[t] <= priorities[operators[-1]]:
                output.append(operators.pop())
            operators.append(t)
        elif t == '(':
            operators.append('(')
        else:
            while operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
    while len(operators):
        output.append(operators.pop())
    return ' '.join(output)

print (toRPN('18+4*5*(2+1*3)+2789'))
