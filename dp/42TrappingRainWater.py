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
        sz=len(height)
        ret=0
        if sz:
            rightHMax=height[-1]
            rightHs=[0]*sz
            leftHMax=height[0]
            for i in reversed(xrange(0, sz)):
                rightHMax=max(rightHMax, height[i])
                rightHs[i]=rightHMax
            for i in xrange(0, sz):
                if leftHMax>=height[i] and rightHs[i]>=height[i]:
                    ret+=(min(leftHMax, rightHs[i])-height[i])
                else:
                    leftHMax=max(height[i], leftHMax)
        return ret
