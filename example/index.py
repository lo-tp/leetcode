from node import TreeNode
from dfs import Recursion, NonRecursion

'''
    1
 2     3
4 5   6 7
'''

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

print 'DFS Recursion'
dfsRecursion=Recursion()

print 'Pre Order'
dfsRecursion.preOrder(root)

print 'In Order'
dfsRecursion.inOrder(root)

print 'DFS NonRecursion'
dfsNonRecursion=NonRecursion()

print 'Pre Order'
dfsNonRecursion.preOrder(root)

print 'In Order'
dfsNonRecursion.inOrder(root)
