class Solution(object):
    def sumRootToLeaf(self, root):
        res = 0
        if root:
            stack = [[root]]
            while stack:
                path = stack.pop()
                if path[-1].left:
                    new_path = path[:]
                    new_path.append(path[-1].left)
                    stack.append(new_path)
                elif path[-1].right:
                    new_path = path[:]
                    new_path.append(path[-1].right)
                    stack.append(new_path)
                else:
                    tmp = 1
                    for i in path:
                        res += i.val*tmp
                        print res
                        tmp *= 2
        return res
