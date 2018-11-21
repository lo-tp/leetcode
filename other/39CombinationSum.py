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
