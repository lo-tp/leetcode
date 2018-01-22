
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)

class Solution(object):
    def tree2str(self, t1):
        stack=[t1]
        str=''
        while len(stack) is not 0:
            k=stack[-1]
            if k is not None:
                if hasattr(k, 'visited'):
                    str+=')'
                    stack.pop()
                else:
                    str='%s(%d'% (str, k.val)
                    k.visited=True
                    if k.left is not None or k.right is not None:
                        if k.right is not None:
                            stack.append(k.right)
                        stack.append(k.left)
            else:
                str+='()'
                stack.pop()
        return str[1:-1]
soluction = Solution()
print soluction.tree2str(root)
