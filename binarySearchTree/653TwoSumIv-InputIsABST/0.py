
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def makeBTFromArray(array):
    list = []
    index = 0
    for i in array:
        print "%d: " % (index),
        print i
        index+=1
        if i is not None:
            list.append(TreeNode(i))
        else:
            list.append(None)
    size=len(list)
    for i in range(size):
        if list[i] is not None:
            lIndex=i*2+1
            rIndex=i*2+2
            if lIndex<=size and list[lIndex] is not None:
                list[i].left=list[lIndex]
            if rIndex<=size and list[rIndex] is not None:
                list[i].right=list[rIndex]
    return list[0]




class Solution(object):
    def find(self, root, target, original):
        stack=[root]
        while len(stack):
            node=stack.pop()
            if node.val == target and original is not node:
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False

    def findTarget(self, root, k):
        stack=[root]
        while len(stack):
            node=stack.pop()
            if self.find(root, k-node.val, node) is True:
                return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False

root=makeBTFromArray([-48,None,20,7,39,-6,19,30,42,-25,-3,11,None,22,35,41,49,-33,-15,-5,1,9,12,None,29,34,38,None,None,47,None,-43,-32,-18,-13,None,None,0,2,None,10,None,None,27,None,None,None,None,None,45,None,-46,-40,None,-26,-21,-17,-14,-8,None,None,None,4,None,None,23,None,44,None,None,None,None,-37,-28,None,None,None,None,-16,None,None,None,None,None,None,None,24,None,None,None,-36,-31])

soluction = Solution()
print soluction.find2Target(root, -64)
