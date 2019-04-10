class Solution(object):
    def buildTreeNonRecursion(self, preorder, inorder):
        dumbNode = TreeNode(0)
        stack = [(0, 0, len(preorder), dumbNode, False)]
        while stack:
            inStart, preStart, size, parentNode, isRight = stack.pop()
            if size:
                inEnd = inStart+size-1
                while inOrder[inEnd] != preorder[preStart]:
                    inEnd -= 1
                rightSize = inStart+size-1-inEnd
                leftSize = size-rightSize-1
                newNode = TreeNode(preorder[preStart])
                if isRight:
                    parentNode.right = newNode
                else:
                    parentNode.left = newNode
                stack.append((inStart, preStart+1, leftSize, newNode, False))
                stack.append((inStart+leftSize+1, preStart +
                              leftSize+1, rightSize, newNode, True))
        return dumbNode.left
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
