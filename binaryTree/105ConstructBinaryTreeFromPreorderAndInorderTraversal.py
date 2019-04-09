class Solution(object):
    def build(self, inStart, preStart, size):
        print preStart, inStart
        ret = TreeNode(self.preOrder[preStart])
        if size != 1:
            inEnd = inStart+size-1
            while self.inOrder[inEnd] != self.preOrder[preStart]:
                inEnd -= 1
            rightSize = inStart+size-inEnd-1
            leftSize = size-rightSize-1
            if leftSize:
                ret.left = self.build(inStart, preStart+1, leftSize)
            if rightSize:
                ret.right = self.build(
                    inStart+1+leftSize, preStart+1+leftSize, rightSize)
        return ret

    def buildTree(self, preorder, inorder):
        self.inOrder, self.preOrder = inorder, preorder
        return self.build(0, 0, len(preorder)) if preorder else None
