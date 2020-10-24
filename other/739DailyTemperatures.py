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

    def dailyTemperaturesLessSpace(self, T):
        res, size = [], len(T)
        if size:
            stack, res = [0], [0]*size
            for current in xrange(1, size):
                while stack and T[stack[-1]] < T[current]:
                    prev_index = stack.pop()
                    res[prev_index] = current-prev_index
                stack.append(current)
        return res
    def dailyTemperatures(self, T):
        res, stack = [0 for i in T], []
        for i in range(len(T)-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]-i
            stack.append(i)
        return res

