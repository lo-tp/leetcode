class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            lD=self.maxDepth(root.left)+1
            rD=self.maxDepth(root.right)+1
            return lD if lD>rD else rD
        return 0
