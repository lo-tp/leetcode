def remove(nums, k):
    l, sz, count = 0, len(nums), 1
    if sz <= k:
        return sz
    while l+1 < sz and count <= k:
        l += 1
        if nums[l] != nums[l-1]:
            count = 0
        count += 1
    r = l+1
    if l+1 == sz:
        return l+1 if count <= k else l
    while r < sz:
        if nums[r] != nums[r-1]:
            count = 0
        count += 1
        if count <= k:
            nums[l] = nums[r]
            l += 1
        r += 1
    return l


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
        return res

    def removeDuplicates(self, nums):
        return remove(nums, 2)
