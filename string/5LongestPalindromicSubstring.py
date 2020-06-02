from re import sub

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
    def longestPalindrome(self, s):
        maximum, res, t = 0, 0, '-{}-'.format('-'.join(list(s)))
        sz, l, m, r = len(t), 0, 0, 0
        data = [0]*sz
        for i in xrange(0, sz):
            mirror_i = 2*m-i
            if mirror_i < m and mirror_i >= l:
                data[i] = min(data[mirror_i], r-i)
            l_edge, r_edge = i-data[i]-1, i+data[i]+1
            while l_edge > -1 and r_edge < sz and t[l_edge] == t[r_edge]:
                l_edge -= 1
                r_edge += 1
                data[i] += 1
            if r_edge-1 > r:
                l, m, r = l_edge+1, i, r_edge-1
            if data[i] > maximum:
                maximum, res = data[i], i
        return sub('-', '', t[res-data[res]: res+data[res]+1])
