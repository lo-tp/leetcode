class Solution(object):
    def dailyTemperatures(self, T):
        res = []
        if T:
            stack, res = [(-1, T[0])], T[:]
            for index, temp in enumerate(T[1:]):
                while stack and temp > stack[-1][1]:
                    old_index, _ = stack.pop()
                    res[old_index+1] = index-old_index
                stack.append((index, temp))
            for index, _ in stack:
                res[index+1] = 0
        return res
