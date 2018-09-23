class Solution(object):
    def dfs(self, root):
        if not root:
            return [0,0]
        else:
            l,r=self.dfs(root.left), self.dfs(root.right)
            return [root.val+l[1]+r[1], max(l)+max(r)]
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
