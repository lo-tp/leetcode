def findCombinations(candidates, size, target, currentSum, path, startIndex, res):
    if currentSum==target:
        res.append(path)
        return;
    if currentSum>target:
        return
    for i in xrange(startIndex, size):
        findCombinations(candidates, size, target, currentSum+candidates[i], path+[candidates[i]], i, res)

class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        findCombinations(candidates, len(candidates), target, 0, [], 0, res)
        return res
class Solution(object):
    def combinationSum(self, candidates, target):
        current, sz, res, total = [], len(candidates), [], 0
        stack = [(i, False) for i in range(0, sz)]
        while stack:
            index, visited = stack.pop()
            if visited:
                if total == target:
                    res.append(current[:])
                total -= candidates[index]
                current.pop()
            else:
                total += candidates[index]
                current.append(candidates[index])
                stack.append((index, True))
                if total < target:
                    stack.extend([(i, False) for i in range(index, sz)])
        return res
