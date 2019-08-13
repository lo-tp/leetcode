class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        size, res = len(difficulty), 0
        indexes = sorted([index for index, dif in enumerate(
            difficulty)], key=lambda i: -profit[i])
        i = 0
        for w in sorted(worker, key lambda k: -k):
            while i < size and difficulty[indexes[i]] > w:
                i += 1
            if i == size:
                break
            else:
                res += profit[i]
        return res
