from node import TreeNode

class Recursion(object):
    def preOrder(self, r):
        print r.val
        if(r.left):
            self.preOrder(r.left)
        if(r.right):
            self.preOrder(r.right)

    def inOrder(self, r):
        if(r.left):
            self.inOrder(r.left)
        print r.val
        if(r.right):
            self.inOrder(r.right)

class NonRecursion(object):
    def preOrder(self, r):
        stack=[r]
        while len(stack):
            t=stack.pop()
            if(t):
                print t.val
            if(t.right):
                stack.append(t.right)
            if(t.left):
                stack.append(t.left)

    def inOrder(self, r):
        done=0
        stack=[]
        current=r
        while not done:
          if current is not None:
              stack.append(current)
              current=current.left
          else:
              if len(stack):
                  t=stack.pop()
                  print t.val
                  current=t.right
              else:
                   done=1
