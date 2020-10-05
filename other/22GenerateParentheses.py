class Solution(object):
    def generateParenthesis(self, n):
        ret=[]
        dict={}
        for i in xrange(0,n):
            tmp=[]
            for x in ret:
                for w in xrange(0,i*2):
                    newData=x[:w]+['(',')']+x[w:]
                    str=''.join(newData)
                    if str not in dict:
                        dict[str]=True
                        tmp.append(newData)
            if ret:
                newData=['(']+ret[-1]+[')']
            else:
                newData=['(',')']
            str=''.join(newData)
            if str not in dict:
                dict[str]=True
                tmp.append(newData)
            ret=tmp
        return map(lambda x:''.join(x), ret)
    def generateParenthesis(self, n):
        current, res, stack, l, r = [], [], [('(', False)], 0, 0
        while stack:
            option, visited = stack.pop()
            if visited:
                if l == r == n:
                    res.append(''.join(current))
                if current[-1] == '(':
                    l -= 1
                else:
                    r -= 1
                current.pop()
            else:
                stack.append((option, True))
                if option == '(':
                    l += 1
                else:
                    r += 1
                if l >= r and l <= n:
                    if l < n:
                        stack.append(('(', False))
                    if r < n:
                        stack.append((')', False))
                current.append(option)
        return res
