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

