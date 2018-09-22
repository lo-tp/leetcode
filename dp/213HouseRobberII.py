class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        if size==0:
            return 0
        elif size==1:
            return nums[0]
        else:
            records=[(0,0)]*size
            records[0]=(0,nums[0])
            records[1]=(nums[1], max(nums[1],nums[0]))
            index=2
            while index<size:
                records[index]=(max(records[index-2][0]+nums[index], records[index-1][0]),
                                max(records[index-2][1]+nums[index], records[index-1][ 1 ]))
                index+=1
            return max(records[index-1][0], records[index-2][1])
s=Solution()
print s.rob([2,1,1,2])
