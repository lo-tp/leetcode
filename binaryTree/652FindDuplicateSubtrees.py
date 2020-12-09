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
    def findDuplicateSubtrees(self, root):
        res, current, stack, data = [], '', [
            (root, 0, '')], defaultdict(lambda: 0)
        while stack:
            root, flag, left_str = stack.pop()
            if not root:
                current += ' '
            elif not flag:
                stack.append((root, 1, ''))
                stack.append((root.left, 0, ''))
            elif flag == 1:
                stack.append((root, 2, current))
                stack.append((root.right, 0, ''))
                current = ''
            else:
                current = 'l{}-{}-{}r'.format(left_str, root.val, current)
                if data[current] == 1:
                    res.append(root)
                data[current] += 1
        return res

    def findDuplicateSubtrees(self, root):
        cur = None
        res, data, stack = [], defaultdict(lambda: 0), [(root, None, 0)]
        while stack:
            node, string, flag = stack.pop()
            if not node:
                cur = '#'
            elif not flag:
                stack.append((node, None, 1))
                stack.append((node.left, None, 0))
            elif flag == 1:
                stack.append((node, cur, 2))
                stack.append((node.right, None, 0))
            else:
                cur = '{},{},{}'.format(node.val, string, cur)
                data[cur] += 1
                if data[cur] == 2:
                    res.append(node)
        return res
