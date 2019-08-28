class Solution(object):
    def smallestRepunitDivByK(self, K):
        r, i, s = 1 % K, 1, set()
        while r:
            r = (r*10+1) % K
            if r in s:
                return -1
            i += 1
            s.add(r)
        return i
