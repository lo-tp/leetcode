class Solution(object):
    def sumNumbers(self, root):
        res, stack = 0, []
        if root:
            stack.append((root, root.val))
            while stack:
                t, val = stack.pop()
                if t.left or t.right:
                    if t.left:
                        stack.append((t.left, val*10+t.left.val))
                    if t.right:
                        stack.append((t.right, val*10+t.right.val))
                else:
                    res += val
        return res
