class Solution(object):
    def findMaxLength(self, nums):
        k, res, data = 0, 0, {0: 0}
        for i, j in enumerate(nums):
            if j:
                k += 1
            else:
                k -= 1
            if not k:
                res = max(i+1, res)
            elif k in data:
                res = max(res, i-data[k])
            else:
                data[k] = i
        return res

