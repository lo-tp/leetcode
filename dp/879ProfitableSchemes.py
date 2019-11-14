from copy import deepcopy


class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        mod, res, size = pow(10, 9)+7, 0, len(profit)
        data = sorted([[profit[i], group[i]]
                       for i in xrange(0, size)], key=lambda k: -k[0]/k[1])
        sums = deepcopy(data)
        for i in xrange(1, size):
            sums[i][0] += sums[i-1][0]
            sums[i][1] += sums[i-1][1]
        for i in xrange(0, size):
            sums[i][0] = sums[-1][0]-sums[i][0]
            sums[i][1] = sums[-1][1]-sums[i][1]
        stack = [(0, G, P)]
        print data
        if data[0][1] <= G:
            stack.append((0, G-data[0][1], P-data[0][0]))
        while stack:
            print stack
            index, g, p = stack.pop()
            if p <= 0:
                res += pow(2, size-index-1)
            elif g >= sums[index][1] and p <= sums[index][0]:
                index += 1
                stack.append((index, g-data[index][1], p-data[index][0]))
                stack.append((index, g, p))
        return res % mod

