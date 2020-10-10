class Solution(object):
    def findTarget(self, root, k):
        data, stack = set(), []
        while stack or root:
            if root:
                stack.append((root, False))
                root = root.left
            else:
                root, visited = stack.pop()
                if visited:
                    if k-root.val in data:
                        return True
                    data.add(root.val)
                    root = None
                else:
                    stack.append((root, True))
                    root = root.right
        return False
