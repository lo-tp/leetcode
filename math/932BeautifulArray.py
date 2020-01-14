class Solution(object):
    def beautifulArray(self, N):
        stack, i = [], N
        while i > 1:
            stack.append(i)
            i = i/2+i % 2
        res = [1]
        for j in xrange(len(stack)-1, -1, -1):
            j = stack[j]
            tmp = []
            for i in res:
                tmp.append(i*2-1)
            for i in res:
                tmp.append(i*2)
            if j % 2:
                res = filter(lambda k: k != j+1, tmp)
            else:
                res = tmp
        return res
