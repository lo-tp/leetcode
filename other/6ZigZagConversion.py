class Solution(object):
    def convert(self, s, numRows):
        sz, res, index, row_index = len(
            s), [[] for _ in range(0, numRows)], 0, 0
        while index < sz:
            while index < sz and row_index < numRows:
                res[row_index].append(s[index])
                index += 1
                row_index += 1
            row_index -= 2
            while index < sz and row_index > 0:
                res[row_index].append(s[index])
                index += 1
                row_index -= 1
        return ''.join([''.join(row) for row in res])

    def convert(self, s, numRows):
        if numRows > 1:
            sz, res, cycle_sz = len(s), [], 2*numRows-2
            i = 0
            while i < sz:
                res.append(s[i])
                i += cycle_sz
            i, j = 1, 2*numRows-3
            for _ in range(0, numRows-2):
                t = 0
                while True:
                    if t+i < sz:
                        res.append(s[t+i])
                    else:
                        break
                    if t+j < sz:
                        res.append(s[t+j])
                    else:
                        break
                    t += cycle_sz
                i += 1
                j -= 1
            i = numRows-1
            while i < sz:
                res.append(s[i])
                i += cycle_sz
            return ''.join(res)
        return s
    def convert(self, s: str, numRows: int) -> str:
        data = [[] for _ in range(0, numRows)]
        index = [idx for idx in range(0, numRows)]
        for idx in range(numRows - 2, 0, -1):
            index.append(idx)
        # print(index)
        for idx in range(0, len(s)):
            data[index[idx % len(index)]].append(s[idx])
        # print(data)
        return "".join(["".join(r) for r in data])

