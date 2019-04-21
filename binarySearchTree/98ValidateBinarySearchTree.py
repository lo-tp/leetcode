from sys import maxint


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
