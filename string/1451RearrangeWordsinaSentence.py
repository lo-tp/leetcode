from collections import defaultdict


class Solution(object):
    def arrangeWords(self, text):
        data = defaultdict(lambda: [])
        for i in text.split(' '):
            data[len(i)].append(i)
        res = ' '.join([' '.join(data[k])
                        for k in sorted(data.keys())]).lower()
        return '{}{}'.format(res[0].upper(), res[1:])
