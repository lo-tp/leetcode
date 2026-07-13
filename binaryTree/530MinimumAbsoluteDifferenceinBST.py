class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack, prev, res=[(root, False)], -float('inf'), float('inf')
        while stack:
            n,visited=stack.pop()
            if visited:
                res=min(abs(n.val-prev),res)
                prev=n.val
            else:
                if n.right:
                    stack.append((n.right, False))
                stack.append((n,True))
                if n.left:
                    stack.append((n.left, False))
        return res
