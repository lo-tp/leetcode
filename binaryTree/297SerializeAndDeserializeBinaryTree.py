import json


class Codec:

    def serialize(self, root):
        tmp1, res,  tmp2 = [root], [], []
        while tmp1:
            for i in tmp1:
                if i:
                    res.append(i.val)
                    tmp2.append(i.left)
                    tmp2.append(i.right)
                else:
                    res.append(None)
                    tmp2.append(None)
                    tmp2.append(None)
            flag = False
            for i in tmp2:
                if i:
                    flag = True
            if flag:
                tmp1 = tmp2
                tmp2 = []
            else:
                tmp1 = None
        return json.dumps(res)

    def deserialize(self, data):
        tmp = map(lambda x: TreeNode(x) if x else None, json.loads(data))
        for i in xrange(0, (len(tmp)-2)/2):
            if tmp[i]:
                tmp[i].left = tmp[i*2+1]
                tmp[i].right = tmp[i*2+2]
        return tmp[0]

    def serialize(self, root):
        data = []
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if prev.right:
                    root = root.right
                    data.append(None)
                    prev.right = None
                else:
                    prev.right = root
                    data.append(root.val)
                    root = root.left
            else:
                data.append(root.val)
                data.append(None)
                root = root.right
        data.append(None)
        return json.dumps(data)

    def deserialize(self, data):
        arr = [TreeNode(i) if i is not None else i for i in json.loads(data)]
        arr = [{'node': i} for i in arr]
        stack = [arr[0]]
        for i in arr[1:]:
            if 'flag' in stack[-1]:
                stack[-1]['node'].right = i['node']
                stack.pop()
            else:
                stack[-1]['node'].left = i['node']
                stack[-1]['flag'] = 1
            if i['node']:
                stack.append(i)
        return arr[0]['node']

    def serialize(self, root):
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            if not root:
                res.append('#')
            else:
                res.append('{}'.format(root.val))
                stack.append(root.right)
                stack.append(root.left)
        return ','.join(res)

    def deserialize(self, data):
        index, cur, stack = 0, None, [(None, 0)]
        data = data.split(',')
        while stack:
            node, flag = stack.pop()
            if not flag:
                if data[index] == '#':
                    cur = None
                else:
                    cur = TreeNode(data[index])
                    stack.append((cur, 1))
                    stack.append((None, 0))
                index += 1
            elif flag == 1:
                node.left = cur
                cur = node
                stack.append((node, 2))
                stack.append((None, 0))
            else:
                node.right = cur
                cur = node
        return cur

    def serialize(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            root, flag = stack.pop()
            if not root:
                res.append('#')
            elif not flag:
                stack.append((root, 1))
                stack.append((root.left, 0))
            elif flag == 1:
                stack.append((root, 2))
                stack.append((root.right, 0))
            else:
                res.append(str(root.val))
        return ','.join(res)

    def deserialize(self, data):
        data = data.split(',')
        cur, index, stack = None, len(data)-1, [(None, 0)]
        while stack:
            node, flag = stack.pop()
            if not flag:
                if data[index] == '#':
                    cur = None
                else:
                    cur = TreeNode(data[index])
                    stack.append((cur, 1))
                    stack.append((None, 0))
                index -= 1
            elif flag == 1:
                node.right = cur
                cur = node
                stack.append((cur, 2))
                stack.append((None, 0))
            else:
                node.left = cur
                cur = node
        return cur

    def serialize(self, root):
        res, tmp, stack = [], [], [root]
        while stack:
            for t in stack:
                if not t:
                    res.append('#')
                else:
                    res.append(str(t.val))
                    tmp.append(t.left)
                    tmp.append(t.right)
            stack, tmp = tmp, []
        return ','.join(res)

    def deserialize(self, data):
        data = data.split(',')
        stack, sz = [], len(data)
        res = None
        if data:
            index, i, res = 0, 1, TreeNode(data[0])
            stack.append(res)
            while i < sz:
                prev_node = stack[index]
                node = None if data[i] == '#' else TreeNode(data[i])
                prev_node.left = node
                i += 1
                node = None if data[i] == '#' else TreeNode(data[i])
                prev_node.right = node
                i += 1
                if prev.left:
                    stack.append(prev.left)
                if prev.right:
                    stack.append(prev.right)
                index += 1
        return res

    def deserialize(self, data):
        data = data.split(',')
        sz = len(data)
        if sz:
            stack = []
            for i in data:
                if i == '#':
                    stack.append(None)
                else:
                    node = TreeNode(i)
                    node.right = stack.pop()
                    node.left = stack.pop()
                    stack.append(node)
            return stack[0]
        return None

    def serialize(self, root):
        data = []
        if root:
            stack = []
            while root or stack:
                if root:
                    data.append(str(root.val))
                    stack.append(root)
                    root = root.left
                else:
                    data.append('#')
                    root = stack.pop().right
            data.append('#')
        return ','.join(data)

    def deserialize(self, data):
        data = data.split(',')
        sz = len(data)
        if sz:
            cur, stack = None, []
            for i in data:
                node = None if i == '#' else TreeNode(i)
                if node:
                    stack.append((node, False))
                else:
                    cur, flag = stack.pop()
                    if flag:
                        t = cur
                        while stack and stack[-1][1]:
                            cur, _ = stack.pop()
                            cur.right = t
                            t = cur
                        if stack:
                            cur, _ = stack.pop()
                            cur.left = t
                            stack.append((cur, True))
                    else:
                        stack.append((cur, True))
            return cur
        return None
