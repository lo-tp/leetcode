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
    def sumNumbersInOrderDfs(self, root):
        res, stack = 0, []
        while root or stack:
            if root:
                if root.left:
                    root.left.val += root.val*10
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if not root.left and not root.right:
                    res += root.val
                if root.right:
                    root.right.val += root.val*10
                root = root.right
        return res

