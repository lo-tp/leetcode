class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        res, sz, index, stack = [], len(voyage), 0, []
        while index < sz and (root or stack):
            if root:
                if voyage[index] != root.val:
                    res = [-1]
                    break
                index += 1
                if index < sz:
                    if not root.left or root.left.val != voyage[index]:
                        res.append(root.val)
                        root.left, root.right = root.right, root.left
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return res
