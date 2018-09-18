class Solution(object):
    def manacher(self, s):
        processedString='#'+'#'.join(list(s))+'#'
        size=len(processedString)
        palindromicLength=[0]*size
        centerIndex=0
        rightIndex=0
        index=0
        while index<size:
            mirrorIndex=2*centerIndex-index
            if mirrorIndex>=0:
                rightLength=rightIndex-index
                if palindromicLength[mirrorIndex]>rightLength:
                    palindromicLength[index]=rightLength
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
        return palindromicLength;
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromicLength=self.manacher(s)
        maxIndex=0
        index=0
        size=len(palindromicLength)
        while index<size:
            if palindromicLength[index]>palindromicLength[maxIndex]:
                maxIndex=index
            index+=1
        realIndex=maxIndex/2
        maxPalindromicLength=palindromicLength[maxIndex]
        startIndex=realIndex-maxPalindromicLength/2
        endIndex=realIndex+maxPalindromicLength/2 + maxPalindromicLength%2;
        return s[startIndex:endIndex]
