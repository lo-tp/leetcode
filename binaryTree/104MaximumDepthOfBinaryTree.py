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
def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        current_level = [root]
        
        while current_level:
            level += 1
            # Build the next level using only valid children
            current_level = [
                child 
                for node in current_level 
                for child in (node.left, node.right) 
                if child
            ]
            
        return level
