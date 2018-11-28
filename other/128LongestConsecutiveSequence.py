def qc(nums, start, end):
    s, e, m = start, end, nums[start+(end-start)/2]
    while s <= e:
        while nums[s] < m:
            s += 1
        while nums[e] > m:
            e -= 1
        if s <= e:
            if nums[s] != nums[e]:
                nums[s] = nums[s] ^ nums[e]
                nums[e] = nums[s] ^ nums[e]
                nums[s] = nums[s] ^ nums[e]
            s += 1
            e -= 1
    if s < end:
        qc(nums, s, end)
    if start < e:
        qc(nums, start, e)


class Solution(object):
    def longestConsecutive1(self, nums):
        data, res, sz = set(nums), 0, len(nums)
        if sz:
            res = 1
            for i in nums:
                if i-1 not in data:
                    k = i+1
                    while k in nums:
                        k += 1
                    res = max(res, k-i)
        return res

    def longestConsecutive(self, nums):
        res, currentLongest, index, sz = 1, 1, 1, len(nums)
        if sz:
            res = 1
            qc(nums, 0, sz-1)
            while index < sz:
                if nums[index-1]+1 == nums[index]:
                    currentLongest += 1
                else:
                    res = max(res, currentLongest)
                    currentLongest = 1
                index += 1
            print nums
        return res
