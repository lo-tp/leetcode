from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self, root):
        res, current, stack, data = [], '', [], defaultdict(lambda: 0)
        while stack or root:
            if root:
                stack.append((root, False, ''))
                root = root.left
            else:
                t, visited, left_str = stack.pop()
                if visited:
                    current = '{} {} {}'.format(left_str, t.val, current)
                    root = None
                    if data[current] == 1:
                        res.append(t)
                    data[current] += 1
                else:
                    stack.append((t, True, current))
                    current = ''
                    root = t.right
        return res
