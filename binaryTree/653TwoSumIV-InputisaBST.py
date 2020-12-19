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

class Solution(object):
    def findTarget(self, root, k):
        data, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                data.append(root.val)
                root = root.right
        l, r = 0, len(data)-1
        while l < r:
            t = data[l]+data[r]
            if t > k:
                r -= 1
            elif t < k:
                l += 1
            else:
                return True
        return False
