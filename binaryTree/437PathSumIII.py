class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root:
            return 0
        seen = defaultdict(lambda: 0)
        seen[0] += 1
        stack = [(root, root.val, False)]
        res = 0
        while stack:
            n, cur, visited = stack.pop()
            print(cur,visited)
            if not visited:
                offset = cur - targetSum
                res += seen[offset]
                seen[cur] += 1
                stack.append((n, cur, True))
                if n.left:
                    stack.append((n.left, cur + n.left.val, False))
                if n.right:
                    stack.append((n.right, cur + n.right.val, False))
            else:
                seen[cur] -= 1
        return res
