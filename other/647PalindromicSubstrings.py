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
