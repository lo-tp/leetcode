class Solution(object):
    def distanceK(self, root, target, K):
        seen, stack,  depth = set(), [root], 0
        root.parent=None
        while root or stack:
            if root:
                stack.append(root)
                if root.left:
                    root.left.parent = root
                root = root.left
            else:
                root = stack.pop()
                if root.right:
                    root.right.parent = root
                root = root.right
        stack = [target]
        seen.add(target)
        while stack:
            if depth == K:
                return [i.val for i in stack]
            t = []
            for i in stack:
                if i.left and i.left not in seen:
                    t.append(i.left)
                    seen.add(i.left)
                if i.right and i.right not in seen:
                    t.append(i.right)
                    seen.add(i.right)
                if i.parent and i.parent not in seen:
                    t.append(i.parent)
                    seen.add(i.parent)
            depth += 1
            stack = t
        return []
