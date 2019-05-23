class BSTIterator(object):

    def __init__(self, root):
        self.root = root

    def next(self):
        ret = None
        while True:
            if self.root.left:
                pre = self.root.left
                while pre.right and pre.right != self.root:
                    pre = pre.right
                if pre.right:
                    ret = self.root.val
                    self.root = self.root.right
                    pre.right = None
                    break
                else:
                    pre.right = self.root
                    self.root = self.root.left
            else:
                ret = self.root.val
                self.root = self.root.right
                break
        return ret

    def hasNext(self):
        return self.root

    // with stack
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        root = tmp = self.stack.pop()
        tmp = tmp.right
        while tmp:
            self.stack.append(tmp)
            tmp = tmp.left
        return root.val

    def hasNext(self):
        return self.stack
