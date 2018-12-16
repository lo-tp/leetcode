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
