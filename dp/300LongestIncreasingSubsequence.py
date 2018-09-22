class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records=[]
        max=0
        size=len(nums)
        if size:
            max=1
            records.append((1,nums[0]))
            for i in xrange(1, size):
                currentMax=1
                for (previousMax, previousNumber) in records:
                    if previousMax>=currentMax and nums[i]>previousNumber:
                        currentMax=previousMax+1
                if currentMax>max:
                    max=currentMax
                records.append((currentMax, nums[i]))
        return max
    # time complexity: nlogn
    def lengthOfLISBetter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        if len(nums):
            records=[nums[0]]
            ret+=1
            for x in xrange(1,len(nums)):
                i=nums[x]
                if i>records[-1]:
                    records.append(i)
                    ret+=1
                elif i<=records[0]:
                    records[0]=i
                else:
                    s=0
                    e=ret-1
                    while s<=e:
                        m=s+(e-s)/2
                        if m==0 or i>records[m]:
                            s=m+1
                        elif i<=records[m-1]:
                            e=m-1
                        else:
                            records[m]=i
                            break
        return ret
