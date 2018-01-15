# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

def tupleMaker(parent1,parent2, name):
    t1 = None
    t2 = None
    if name is 'left':
        if parent1 is not None:
            t1 = parent1.left
        if parent2 is not None:
            t2 = parent2.left
    else:
        if parent1 is not None:
            t1 = parent1.right
        if parent2 is not None:
            t2 = parent2.right
    if t1 is None and t2 is None:
        return None
    if t1 is None:
        return (t2, t1)
    else:
        return (t1, t2)

class Solution(object):
    def mergeTrees(self, t1, t2):
        root = None
        if t1 is None and t2 is None:
            return root
        if t1 is None:
            root = (t2, t1)
        else:
            root = (t1,t2)
        stack = []
        stack.append(root)

        while len(stack):
            tem = stack.pop()
            element1 = tem[0]
            element2 = tem[1]
            if element2 is not None:
                element1.val += element2.val
            lTuple=tupleMaker(element1, element2, 'left')
            if lTuple is not None:
                element1.left=lTuple[0]
                stack.append(lTuple)
            rTuple=tupleMaker(element1, element2, 'right')
            if rTuple is not None:
                element1.right=rTuple[0]
                stack.append(rTuple)

        return root[0]

soluction = Solution()
print soluction.mergeTrees(root,root).val
