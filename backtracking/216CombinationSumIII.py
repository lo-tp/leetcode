class Solution(object):
    def combinationSum3(self, k, n):
        res, stack, current, total = [], [
            (i, False) for i in range(1, 11-k)], [], 0
        while stack:
            num, visited = stack.pop()
            if visited:
                if len(current) == k and total == n:
                    res.append(current[:])
                total -= current.pop()
            else:
                stack.append((num, True))
                current.append(num)
                total += num
                if total < n and len(current) < k:
                    num += 1
                    stack.extend([(i, False)
                                  for i in range(num, 11+len(current)-k)])
