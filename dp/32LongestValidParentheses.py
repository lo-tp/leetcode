class Solution(object):
    def longestValidParentheses2(self, str):
        ret=0
        left=0
        right=0
        for i in str:
            if i=='(':
                left+=1
            else:
                right+=1
            if left==right:
                ret=max(ret, right*2)
            elif right>left:
                right=0
                left=0

        right=0
        left=0
        for i in str[::-1]:
            if i=='(':
                left+=1
            else:
                right+=1
            if left==right:
                ret=max(ret, right*2)
            elif left>right:
                right=0
                left=0
        return ret
    def longestValidParentheses(self, str):
        ret=0
        s=[-1]
        index=0
        size=len(str)
        while index<size:
            if str[index]=='(':
                s.append(index)
            else:
                s.pop()
                if len(s)==0:
                    s.append(index)
                ret=max(ret, index-s[-1])
            index+=1
        return ret

    def longestValidParentheses1(self, str):
        size=len(str)
        data=[0]*size
        previousIndex=-1
        for index in xrange(0, size):
            if str[index] ==')':
                leftIndex=index-1
                if leftIndex>=0:
                    if str[leftIndex]=='(':
                        data[index]=2
                        previousIndex=index-2
                    else:
                        if data[leftIndex]>0:
                            pairIndex=index-data[leftIndex]-1
                            if pairIndex>=0 and str[pairIndex]=='(':
                                data[index]=data[leftIndex]+2
                                previousIndex=index-data[index]
            if previousIndex>=0 and data[index]:
                data[index]+=data[previousIndex]

        return max(data) if data else 0
