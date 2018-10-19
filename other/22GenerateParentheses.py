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

s=Solution()
print s.generateParenthesis(1)
