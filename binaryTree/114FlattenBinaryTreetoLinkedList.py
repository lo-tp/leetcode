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
