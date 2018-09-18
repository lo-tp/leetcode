class Solution(object):
    # Time Limit Exceeded
    def countSubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        size=len(s)
        startIndex=0
        while startIndex<size:
            for endIndex in xrange(startIndex, size):
                start=startIndex
                end=endIndex
                while start<=end:
                    if s[start]==s[end]:
                        start+=1
                        end-=1
                    else:
                        break
                if start>end:
                    ret+=1
            startIndex+=1
        return ret
    def countSubstrings(self, s):
        ret=0
        size=len(s)
        startIndex=0
        while startIndex<size:
            start=startIndex
            end=startIndex
            while start>=0 and end<size and s[start]==s[end]:
                ret+=1
                start-=1
                end+=1
            start=startIndex
            end=startIndex+1
            while start>=0 and end<size and s[start]==s[end]:
                ret+=1
                start-=1
                end+=1
            startIndex+=1
        return ret
    # Manacher's algorithm
    def countSubstringsWithManacher(self, s):
        """
        :type s: str
        :rtype: int
        """
        processedString='#'+ '#'.join(list(s))+'#'
        palindromicLength=[0]*len(processedString)
        index=0
        rightIndex=0
        centerIndex=0
        size=len(processedString)
        ret=0
        while index<size:
            mirrorIndex=2*centerIndex-index
            if mirrorIndex>=0:
                if palindromicLength[mirrorIndex]<rightIndex-index:
                    palindromicLength[index]=palindromicLength[mirrorIndex]
                elif palindromicLength[mirrorIndex]>rightIndex-index:
                    palindromicLength[index]=rightIndex-index
                else:
                    palindromicLength[index]=palindromicLength[mirrorIndex]

            leftEdge=index-palindromicLength[index]-1
            rightEdge=index+palindromicLength[index]+1
            while leftEdge>=0 and rightEdge<size and processedString[leftEdge]==processedString[rightEdge]:
                palindromicLength[index]+=1
                leftEdge-=1
                rightEdge+=1

            if index+palindromicLength[index]>rightIndex:
                rightIndex=index+palindromicLength[index]
                centerIndex=index
            index+=1

        return reduce(lambda accu, x: accu+(x+1)/2 ,palindromicLength,  0);
