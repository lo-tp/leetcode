from sys import maxint
from sys import maxsize


class Solution(object):
    def isValidBST(self, root):
        low_end, high_end, stack = -maxint, maxint, []
        while root or stack:
            if root:
                stack.append((root, low_end, high_end))
                high_end = min(high_end, root.val)
                root = root.left
            else:
                root, low_end, high_end = stack.pop()
                if root.val <= low_end or root.val >= high_end:
                    return False
                low_end = max(low_end, root.val)
                root = root.right
        return True

    def isValidBST(self, root):
        hi, low, stack = -maxsize, maxsize, [(root, 0, None)]
        while stack:
            root, flag, t = stack.pop()
            if not root:
                hi, low = -maxsize, maxsize
            elif not flag:
                stack.append((root, 1, None))
                stack.append((root.left, 0, None))
            elif flag:
                if root.val <= hi:
                    return False
                stack.append((root, 2, root.val if low == maxsize else low))
                stack.append((root.right, 0, None))
            else:
                if root.val >= low:
                    return False
                low, hi = t, root.val if hi == -maxsize else hi
        return True
