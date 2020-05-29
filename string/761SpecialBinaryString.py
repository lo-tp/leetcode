class Solution(object):
    def makeLargestSpecialTLE(self, S):
        res = ''

        seen, stack = set(), [S]
        seen.add(S)
        while stack:
            tem = stack.pop()
            seen.add(tem)
            te = 25
            t = [[] for _ in xrange(0, 51)]
            if tem > res:
                res = tem
            t[25].append(-1)
            for i, l in enumerate(tem):
                te += 1 if l == '1' else -1
                t[te].append(i)

            for data in [i for i in t if len(i) > 2]:
                sz = len(data)
                for l_index in xrange(0, sz-2):
                    l = data[l_index]
                    for m_index in xrange(l_index+1, sz-1):
                        m = data[m_index]
                        k = 0
                        for i in xrange(l+1, m+1):
                            k += (1 if tem[i] == '1' else -1)
                            if k < 0:
                                break
                        if k < 0:
                            break
                        for r_index in xrange(m_index+1, sz):
                            r = data[r_index]
                            tmp = "{}{}{}{}".format(
                                tem[:l+1], tem[m+1:r+1], tem[l+1:m+1], tem[r+1:])
                            k = 0
                            for i in xrange(m+1, r+1):
                                k += (1 if tem[i] == '1' else -1)
                                if k < 0:
                                    break
                            if k < 0:
                                break
                            if tmp not in seen:
                                seen.add(tmp)
                                stack.append(tmp)
        return res

    def makeLargestSpecial(self, S):
        data = []
        count, l = 0, 0
        for r, val in enumerate(S):
            count += 1 if val == '1' else -1
            if not count:
                data.append('1{}0'.format(self.makeLargestSpecial(S[l+1:r])))
                l = r+1
        return ''.join(sorted(data)[::-1])
