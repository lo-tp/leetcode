class Solution(object):
    def maxProfit(self, prices):
        size, res, stack = len(prices), 0, [(0, 0, 0, 2, False)]
        while stack:
            index, holding, profit, residue, bought = stack.pop()
            if index < size:
                stack.append((index+1, holding, profit, residue, bought))
                if bought and prices[index] > holding and residue:
                    tmp = profit+prices[index]-holding
                    res = max(res, tmp)
                    stack.append(
                        (index+1, 0, tmp, residue-1, False))
                elif not holding:
                    stack.append(
                        (index+1, prices[index], profit, residue, True))
        return res
