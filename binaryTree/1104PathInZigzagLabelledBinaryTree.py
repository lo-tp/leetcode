class Solution(object):
    def pathInZigZagTree(self, label):
        res, t, flag, s = [], 1, True, 0
        while label > s:
            s += t
            t *= 2
            flag = not flag
        t /= 2
        s -= t
        index = label-s-1
        flag = not flag
        if not flag:
            index = t-1-index
        while t:
            res.append(s+1+index if flag else s+t-index)
            t /= 2
            s -= t
            index /= 2
            flag = not flag
        return res[::-1]

