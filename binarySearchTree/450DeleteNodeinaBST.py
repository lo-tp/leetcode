class Solution(object):
    def deleteNode(self, root, key):
        stack, cur = [(root, 0)], None
        while stack:
            node, flag = stack.pop()
            if not node:
                cur = None
            elif not flag:
                if node.val == key:
                    if node.left and node.right:
                        t = node.left
                        if t.right:
                            while t.right.right:
                                t = t.right
                            te = t.right
                            t.right = t.right.left
                            t = te
                            t.left = node.left
                        t.right = node.right
                        node = t
                    elif node.left:
                        node = node.left
                    elif node.right:
                        node = node.right
                    else:
                        node = None
                else:
                    stack.append((node, 1))
                    stack.append((node.left, 0))
            elif flag == 1:
                node.left = cur
                stack.append((node, 2))
                stack.append((node.right, 0))
            else:
                node.right = cur
            cur = node
        return cur

    def deleteNode(self, root, key):
        res, stack = root, []
        while root and root.val != key:
            if root.val > key:
                stack.append((root, True))
                root = root.left
            else:
                stack.append((root, False))
                root = root.right
        if root:
            if root.left and root.right:
                t = root.left
                if t.right:
                    while t.right.right:
                        t = t.right
                    te = t.right
                    t.right = te.left
                    te.left, te.right = root.left, root.right
                    res = te
                else:
                    res = t
                    t.right = root.right
            elif root.left:
                res = root.left
            elif root.right:
                res = root.right
            else:
                res = None
            while stack:
                node, flag = stack.pop()
                if flag:
                    node.left = res
                else:
                    node.right = res
                res = node
        return res

