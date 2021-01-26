def flatten(root, right):
    if not root and not right:
        return None
    elif not root:
        return flatten(right, None)
    elif not right:
        return flatten(root, root.right)
    else:
        root.right = flatten(root.left, flatten(root.right, right))
        root.left = None
        return root


class Solution(object):
    def flatten(self, root):
        root = flatten(root, None)
    def flattenNonRecursive(self, root):
        if root:
            stack, tmp = [], root
            while True:
                if tmp.left:
                    if tmp.right:
                        stack.append(tmp.right)
                    tmp.right = tmp.left
                    tmp.left = None
                if tmp.right:
                    tmp = tmp.right
                elif stack:
                    tmp.right = stack.pop()
                else:
                    break
    def flatten(self, root):
        stack = []
        if root:
            stack.append(root.right)
            stack.append(root.left)
        while stack:
            node = stack.pop()
            if node:
                root.right = node
                root.left = None
                root = node
                stack.append(node.right)
                stack.append(node.left)
