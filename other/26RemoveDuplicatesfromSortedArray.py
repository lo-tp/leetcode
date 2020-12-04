class Solution(object):
    def removeDuplicatesGeneralWay(self, nums, k):
        res = sz = len(nums)
        if sz > k:
            t, count = nums[0], 1
            for i in range(1, sz):
                if nums[i] != t:
                    t, count = nums[i], 1
                elif count == k:
                    nums[i] = None
                else:
                    count += 1
            t = 0
            while t < sz and nums[t] != None:
                t += 1
            res = t
            te = t+1
            while t < sz and te < sz:
                while te < sz and nums[te] == None:
                    te += 1
                if te < sz:
                    nums[t] = nums[te]
                    nums[te] = None
                    te += 1
                    res += 1
                    t += 1
        return res

    def removeDuplicates(self, nums):
        sz, res = len(nums), 0
        if sz:
            l, r, res = 1, 1, 1
            while r < sz:
                if nums[r] != nums[r-1]:
                    nums[l] = nums[r]
                    l += 1
                    res += 1
                r += 1
        return res

    def removeDuplicates(self, nums):
        sz, slow, fast = len(nums), 1, 1
        while fast < sz:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

    def removeDuplicates(self, nums):
        return self.removeDuplicatesGeneralWay(nums, 1)
