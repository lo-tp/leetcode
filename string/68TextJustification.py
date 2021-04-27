def makeString(tmp, maxWidth, length, is_last=False):
    res, space = '', maxWidth-length
    if len(tmp) == 1:
        res = '{}{}'.format(tmp[0], ' '*space)
    elif is_last:
        res = (' ').join(tmp)
        res += ' '*(maxWidth-length-len(tmp)+1)
    else:
        i, residue, len_space = 0, space % (
            len(tmp)-1), int(space/(len(tmp)-1))
        while i < residue:
            res += '{}{}'.format(tmp[i], ' '*(len_space+1))
            i += 1
        while i < len(tmp)-1:
            res += '{}{}'.format(tmp[i], ' '*len_space)
            i += 1
        res += tmp[-1]
    return res


class Solution(object):
    def fullJustify(self, words, maxWidth):
        sz, tmp, length, res = len(words)-1, [], 0, []
        for i, word in enumerate(words):
            t = len(word)
            length += t
            if length+len(tmp) > maxWidth:
                length -= t
                res.append(makeString(tmp, maxWidth, length))
                tmp = [word]
                length = t
            else:
                tmp.append(word)
        if tmp:
            res.append(makeString(tmp, maxWidth, length, True))
        return res
