class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        stack = [root]
        flag = False
        while stack and not flag:
            tmp = []
            for t in stack:
                if t.left:
                    if flag:
                        return False
                    tmp.append(t.left)
                else:
                    flag = True
                if t.right:
                    if flag:
                        return False
                    tmp.append(t.right)
                else:
                    flag = True
            stack = tmp
        for t in stack:
            if t.left or t.right:
                return False
        return True

    def isCompleteTree(self, root: TreeNode) -> bool:
        stack = [root]
        while stack:
            tmp = []
            for i, t in enumerate(stack):
                if t:
                    tmp.extend([t.left, t.right])
                else:
                    return not (any(stack[i+1:]) or any(tmp))
            stack = tmp
        return True
