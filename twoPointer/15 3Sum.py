def kSum(nums, target, k):
    res, sz = [], len(nums)
    if sz >= k:
        nums.sort()
        w, m = k-2, sz-2
        current, total, stack = [], 0, [(i, False) for i in range(
            0, m) if not i or nums[i] != nums[i-1]]
        while stack:
            index, visited = stack.pop()
            if visited:
                if len(current) == w:
                    l, r, t = current[-1]+1, sz-1, target-total
                    while l <= r:
                        te = nums[l]+nums[r]
                        if te < t:
                            l += 1
                        elif te > t:
                            r -= 1
                        else:
                            if l != r:
                                tem = [nums[i] for i in current]
                                tem.append(nums[l])
                                tem.append(nums[r])
                                res.append(tem)
                            l += 1
                            while l < sz and nums[l] == nums[l-1]:
                                l += 1
                total -= nums[index]
                current.pop()
            else:
                stack.append((index, True))
                total += nums[index]
                current.append(index)
                if len(current) < w:
                    index += 1
                    stack.extend([(i, False) for i in range(
                        index, m) if i == index or nums[i] != nums[i-1]])
    return res
def qc(arr, start, end):
    s, e, m = start, end, arr[(end-start)/2+start]
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            if arr[s] != arr[e]:
                arr[s] = arr[s] ^ arr[e]
                arr[e] = arr[s] ^ arr[e]
                arr[s] = arr[s] ^ arr[e]
            s += 1
            e -= 1
    if s < end:
        qc(arr, s, end)
    if start < e:
        qc(arr, start, e)
    return arr


class Solution(object):
    def threeSum1(self, nums):
        res, sz = [], len(nums)
        if sz >= 3:
            temp = []
            i = 0
            qc(nums, 0, sz-1)
            while i < sz-2:
                l = i+1
                r = sz-1
                while l < r:
                    s = nums[i]+nums[l]+nums[r]
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        print [nums[i], nums[l], nums[r]]
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                i += 1
                while i < sz-2 and nums[i] == nums[i-1]:
                    i += 1
        return res

    def threeSum(self, nums):
        res, sz = [], len(nums)
        if sz >= 3:
            temp = []
            i = 0
            while i < sz-2:
                w = i+1
                while w < sz-1:
                    z = w+1
                    while z < sz:
                        if nums[i]+nums[w]+nums[z] == 0:
                            temp.append([nums[i], nums[w], nums[z]])
                        z += 1
                    w += 1
                i += 1
            temp = map(lambda x: qc(x, 0, 2), temp)
            tmp = {}
            for i in temp:
                tem = '%d %d %d' % (i[0], i[1], i[2])
                if tem not in tmp:
                    res.append(i)
                    tmp[tem] = 0
        return res
    def threeSum(self, nums):
        return kSum(nums, 0, 3)
