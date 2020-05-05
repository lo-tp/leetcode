from collections import Counter


class Solution(object):
    def reorganizeString(self, S):
        sz, res, data = len(S), '', [list(i) for i in sorted(
            Counter(S).items(), key=lambda x: -x[1])]
        d_sz = len(data)
        if data[0][1] <= (sz+1)/2:
            if len(data) > 1:
                flag, tmp = True, [0, 1]
                while True:
                    while (tmp[0] >= d_sz or data[tmp[0]][1]) and (tmp[1] >= d_sz or data[tmp[1]][1]):
                        if flag:
                            res += data[tmp[0]][0]
                            data[tmp[0]][1] -= 1
                        else:
                            res += data[tmp[1]][0]
                            data[tmp[1]][1] -= 1
                        sz -= 1
                        flag = not flag
                    if not sz:
                        break
                    tmp[1 if flag else 0] = max(tmp)+1
            else:
                res += data[0][0]
        return res


