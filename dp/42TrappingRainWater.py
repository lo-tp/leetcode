class Solution(object):
    def trap1(self, height):
        l,r,lMax,rMax,res=0,len(height)-1,0,0,0
        while l<r:
            if height[l]<height[r]:
                if height[l]<lMax:
                    res+=(lMax-height[l])
                else:
                    lMax=height[l]
                l+=1
            else:
                if height[r]<rMax:
                    res+=(rMax-height[r])
                else:
                    rMax=height[r]
                r-=1
        return res
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
