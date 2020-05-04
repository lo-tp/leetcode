class Solution(object):
    def lcaDeepestLeaves(self, root):
        stack = [root]
        root.parent = root
        while True:
            flag, tmp = False, []
            for i in stack:
                if i.left:
                    i.left.parent = i
                    flag = True
                    tmp.append(i.left)
                if i.right:
                    i.right.parent = i
                    flag = True
                    tmp.append(i.right)
            if not flag:
                break
            stack = tmp

        if len(stack)>1:
            while True:
                tmp, seen = [], set()
                for i in stack:
                    seen.add(i.parent.val)
                    tmp.append(i.parent)
                stack = tmp
                if len(seen) == 1:
                    break
        return stack[0]

