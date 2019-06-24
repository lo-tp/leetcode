
class Solution(object):
    def addOneRow(self, root, v, d):
        if d == 1:
            res = TreeNode(v)
            res.left = root
            return res
        stack = [root]
        d -= 2
        while d:
            tmp = []
            while stack:
                k = stack.pop()
                tmp.append(k.left)
                tmp.append(k.right)
            stack = [i for i in tmp if i]
            d -= 1
        for node in stack:
            l, r = node.left, node.right
            node.left, node.right = TreeNode(v), TreeNode(v)
            node.left.left, node.right.right = l, r
        return root
