class Solution(object):
    def jumpFrom(self, index):
        if index == self.sz:
            return True
        for i in xrange(1, self.nums[index]+1).reverse():
            nextIndex = i+index
            if nextIndex not in self.data:
                if self.jumpFrom(nextIndex):
                    return True
                self.data[nextIndex] = True
        return False

    def canJump(self, nums):
        self.sz, self.nums, self.data = len(nums)-1, nums, {}
        if self.sz == -1:
            return False
        return self.jumpFrom(0)

    def canJumpWithoutRecursion(self, nums):
        lastIndex, stack = len(nums)-1, [0]
        while stack:
            k = stack.pop()
            if k >= lastIndex:
                return True
            if nums[k] is not None:
                for i in xrange(k+1, k+nums[k]+1):
                    if i >= lastIndex:
                        return True
                    if nums[i] is not None:
                        stack.append(i)
                nums[k] = None
        return False


s = Solution()
print s.canJump([2, 3, 1, 1, 4])
print s.canJump([3, 2, 1, 0, 4])
print s.canJump([])
