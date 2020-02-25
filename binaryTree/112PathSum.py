class Solution(object):
    def hasPathSum(self, root, sum):
        if root:
            stack = [(root, root.val)]
            while stack:
                node, s = stack.pop()
                if node.left:
                    stack.append((node.left, s+node.left.val))
                if node.right:
                    stack.append((node.right, s+node.right.val))
                if (not node.left) and (not node.right) and s == sum:
                    return True
        return False
