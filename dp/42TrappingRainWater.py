class Solution(object):
    def trap(self, height):
        startIndex=0
        sz=len(height)
        if sz==0:
            return 0
        ret=0
        leftHeight=height[0]
        rightDp=[0]*sz
        rightHeight=height[sz-1]
        for i in reversed(xrange(1, sz-1)):
            rightHeight=max(rightHeight, height[i])
            rightDp[i]=rightHeight

        for i in xrange(1,sz-1):
            leftHeight=max(leftHeight, height[i])
            rightHeight=rightDp[i]
            ret+=(min(leftHeight, rightHeight)-height[i])
        return ret
