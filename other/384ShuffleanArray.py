from random import randrange


class Solution(object):

    def __init__(self, nums):
        self.original = nums

    def reset(self):
        return self.original

    def shuffle(self):
        res = list(self.original)
        sz = len(res)
        for i in xrange(0, sz):
            j = randrange(i, sz)
            res[i], res[j] = res[j], res[i]
        return res
