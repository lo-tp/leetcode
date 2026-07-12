class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            cur = [root]
            while cur:
                tmp = []
                for i in cur:
                    if i.left:
                        tmp.append(i.left)
                    if i.right:
                        tmp.append(i.right)
                res.append(cur[-1].val)
                cur = tmp
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node, depth):
            if not node:
                return
                
            # If this depth equals the length of our result list, it's the first time
            # we are visiting this level! Because we go Right first, this MUST be the rightmost node.
            if depth == len(res):
                res.append(node.val)
                
            # Traverse RIGHT child before LEFT child
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return res
