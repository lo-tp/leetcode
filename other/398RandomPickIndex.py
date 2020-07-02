from collections import defaultdict


class Solution(object):

    def __init__(self, nums):
        self.data = defaultdict(lambda: [])
        self.indexes = defaultdict(lambda: 0)
        for index, num in enumerate(nums):
            self.data[num].append(index)

    def pick(self, target):
        res = self.data[target][self.indexes[target]]
        self.indexs[target] += 1
        self.indexes[target] %= len(self.data[target])
        return res

