class Solution(object):
    def getTreeIterator(self, root):
        while root:
            if root.left:
                pre=root.left
                while pre.right and pre.right!=root:
                    pre=pre.right
                if pre.right:
                    yield root
                    pre.right=None
                    root=root.right
                else:
                    pre.right=root
                    root=root.left
            else:
                yield root
                root=root.right
    def inorderTraversal(self, root):
        iterator=self.getTreeIterator(root)
        return [i.val for i in iterator]
