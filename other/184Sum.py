class Solution(object):
    def fourSum(self, nums, target):
        res, sz = [], len(nums)
        if sz >= 4:
            nums.sort()
            current, total, stack = [], 0, [(i, False) for i in range(
                0, sz-2) if not i or nums[i] != nums[i-1]]
            while stack:
                index, visited = stack.pop()
                if visited:
                    if len(current) == 2:
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
                    if len(current) == 1:
                        index += 1
                        stack.extend([(i, False) for i in range(
                            index, sz-2) if i == index or nums[i] != nums[i-1]])
        return res
