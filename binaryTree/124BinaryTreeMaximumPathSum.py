from sys import maxint


class Solution(object):
    def maxSubTree(self, root):
        res = -maxint
        if root:
            res = root.val
            left_max = self.maxSubTree(root.left)
            right_max = self.maxSubTree(root.right)
            child_max = max(left_max, right_max)
            tmp = res
            if left_max > 0:
                tmp += left_max
            if right_max > 0:
                tmp += right_max
            if child_max > 0:
                res += child_max
            self.res = max(self.res, tmp)
        return res

    def maxPathSum(self, root):
        self.res = -maxint
        self.maxSubTree(root)
        return self.res

    def maxPathSumBetter(self, root):
        res, tmp, stack = -maxint, -maxint, [[None, None, root]]
        while stack:
            left_max, right_max, root = stack[-1]
            if root is None:
                stack.pop()
                tmp = -maxint
            elif left_max is None:
                stack[-1][0] = 'a'
                stack.append([None, None, root.left])
            elif left_max is 'a':
                stack[-1][0] = tmp
            elif right_max is None:
                stack[-1][1] = 'a'
                stack.append([None, None, root.right])
            elif right_max is 'a':
                stack[-1][1] = tmp
            else:
                te = tem = root.val
                if left_max > 0:
                    te += left_max
                if right_max > 0:
                    te += right_max
                res = max(res, te)
                if left_max > 0 or right_max > 0:
                    tem += max(left_max, right_max)
                tmp = tem
                stack.pop()

        return te
