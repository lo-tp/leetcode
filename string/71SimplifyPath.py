class Solution(object):
    def simplifyPath(self, path):
        data = [t for t in path.split('/') if t and t != '.']
        res = []
        for d in data:
            if d == '..':
                if res:
                    res.pop()
            else:
                res.append(d)
        return '{}{}'.format('/', '/'.join(res))
