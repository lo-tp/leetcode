class Solution(object):
    def countNodes(self, root):
        res, stack = 0, [root]
        while stack:
            tmp = []
            while stack:
                k = stack.pop()
                if k:
                    res += 1
                    tmp.append(k.left)
                    tmp.append(k.right)
            stack = tmp
        return res

    def countNodes(self, root: TreeNode) -> int:
        res, stack = 0, []
        while root or stack:
            if stack:
                stack.append(root)
                root = root.left
            else:
                res += 1
                root = stack.pop().right
        return res
