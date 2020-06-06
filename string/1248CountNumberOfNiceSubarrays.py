class Solution(object):
    def numberOfSubarrays(self, nums, k):
        sz, data = len(nums), [0, 0]
        for i, j in enumerate([k-1, k]):
            l, t = 0, 0
            for r in xrange(0, sz):
                if nums[r] % 2:
                    t += 1
                if t > j:
                    while not (nums[l] % 2):
                        l += 1
                    t -= 1
                    l += 1
                if t <= j:
                    data[i] += r-l+1
        return data[1]-data[0]
