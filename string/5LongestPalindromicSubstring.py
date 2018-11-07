class Solution(object):
    def longestPalindrome(self, s):
        str = '#'+'#'.join(list(s))+'#'
        size=len(str)
        dp=[0]*size
        center=0
        right=-1
        ret=0
        for i in xrange(0, size):
            if i <=right:
                pairIndex=center*2-i
                if i+dp[pairIndex]<=right:
                    dp[i]=dp[pairIndex]
                    scanL=i-dp[pairIndex]-1
                    scanR=i+dp[pairIndex]+1
                    while scanL>=0 and scanR<size and str[scanL]==str[scanR]:
                            dp[i]+=1
                            scanL-=1
                            scanR+=1
                else:
                    dp[i]=right-i
            else:
                scanL=i-1
                scanR=i+1
                while scanL>=0 and scanR<size and str[scanL]==str[scanR]:
                        dp[i]+=1
                        scanL-=1
                        scanR+=1
            if i+dp[i]>right:
                center=i
                right=i+dp[i]
            if dp[i]>dp[ret]:
                ret=i
        return str[ret-dp[ret]: ret+dp[ret]+1].replace('#','')
