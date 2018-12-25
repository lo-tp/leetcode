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
        print res
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
