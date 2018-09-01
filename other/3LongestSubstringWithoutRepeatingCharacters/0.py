class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        positions=dict()
        i=0
        j=0
        max=0
        l=len(s)
        while j<l:
            if s[j] in positions and positions[s[j]]>=i:
                i=positions[s[j]]+1
                print i
            positions[s[j]]=j
            max=max if max>j-i+1 else j-i+1
            j+=1
        return max
