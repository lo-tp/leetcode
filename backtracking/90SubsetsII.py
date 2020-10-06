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
