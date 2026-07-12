class Solution:
    def dfs(self, root, depth):
        if not root:
            return None
        if len(self.res)==depth:
            self.res.append([])
        self.res[depth].append(root.val)
        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res=[]
        self.dfs(root,0)
        return self.res

