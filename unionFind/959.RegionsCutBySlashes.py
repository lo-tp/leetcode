class Solution(object):
    def regionsBySlashes(self, grid):
        res, sz = 0, len(grid)
        if sz:
            res += 1
            data = set()
            for v in xrange(0, sz+1):
                data.add('{},{}'.format(v, 0))
                data.add('{},{}'.format(v, sz))
            for h in xrange(1, sz):
                data.add('{},{}'.format(0, h))
                data.add('{},{}'.format(sz, h))
            for v, string in enumerate(grid):
                i = 0
                for h in xrange(0, sz):
                    t = 0
                    if string[i] == '/':
                        te = '{},{}'.format(v+1, h)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                        te = '{},{}'.format(v, h+1)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                    elif string[i] == '\\':
                        te = '{},{}'.format(v, h)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                        te = '{},{}'.format(v+1, h+1)
                        if te in data:
                            t += 1
                        else:
                            data.add(te)
                    i += 1
                    if t == 2:
                        print v, h
                        res += 1
        return res

