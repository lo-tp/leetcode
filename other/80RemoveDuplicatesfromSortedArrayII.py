class Solution(object):
    def removeDuplicates(self, nums):
        res = sz = len(nums)
        if sz > 2:
            t, count = nums[0], 1
            for i in range(1, sz):
                if nums[i] != t:
                    t, count = nums[i], 1
                elif count == 2:
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
        # print(nums)
        return res


