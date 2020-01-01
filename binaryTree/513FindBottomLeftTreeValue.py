class Solution(object):
    def findBottomLeftValue(self, root):
        stack, res = [root], root
        while stack:
            res = stack[0]
            tmp = []
            for i in stack:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            stack = tmp
        return res.val
