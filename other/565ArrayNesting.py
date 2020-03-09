class Solution(object):
    def arrayNesting(self, nums):
        res, seen = 0, set()
        for i, j in enumerate(nums):
            if i not in seen:
                seen.add(i)
                t = 1
                while j not in seen:
                    seen.add(j)
                    j = nums[j]
                    t += 1
                res = max(res, t)
        return res
