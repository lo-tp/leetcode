class Solution(object):
    def subsetsWithDup(self, nums):
        sz, seen, seen_index, t, res = len(nums), set(), set(), [], []
        stack = [(i, False) for i in xrange(0, sz)]
        res.append([])
        seen.add('')
        while stack:
            index, flag = stack.pop()
            if flag:
                seen_index.remove(index)
                t.pop()
            else:
                stack.append((index, True))
                t.append(nums[index])
                te = ''.join([str(i) for i in sorted(t)])
                seen_index.add(index)
                if te not in seen:
                    seen.add(te)
                    res.append(t[:])
                    stack.extend([(i, False)
                                  for i in xrange(0, sz) if i not in seen_index])
        return res

    def subsetsWithDup(self, nums):
        nums.sort()
        sz = len(nums)
        stack, res, current = [(i, False) for i in range(
            0, sz) if not i or nums[i] != nums[i-1]], [[]], []
        while stack:
            index, visited = stack.pop()
            if visited:
                res.append(current[:])
                current.pop()
            else:
                stack.append((index, True))
                current.append(nums[index])
                stack.extend([(i, False) for i in range(index+1, sz)
                              if i == index+1 or nums[i] != nums[i-1]])
        return res

