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
        res = []
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if tmp.right:
                    tmp.right = None
                    root = root.right
                    res.append(None)
                else:
                    res.append(root.val)
                    tmp.right = root
                    root = root.left
            else:
                res.append(root.val)
                res.append(None)
                root = root.right
                if not root:
                    res.append(None)
        return json.dumps(res)

    def deserialize(self, data):
        tmp = map(lambda x: {'node': TreeNode(x)} if x != None else {'node': x}, json.loads(data))
        if tmp:
            stack = [tmp[0]]
            for i in tmp[1:]:
                k = stack[-1]
                if 'l' in k:
                    k['node'].right = i['node']
                    stack.pop()
                else:
                    k['node'].left = i['node']
                    k['l'] = True
                if i['node']:
                    stack.append(i)
            return tmp[0]['node']
        return None
