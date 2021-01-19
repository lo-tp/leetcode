from re import split, match


def isAValidV4Section(arr):
    table = [[1, 2, 3, 4, 4, 4, 4, 4, 4, 4],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
             [6, 6, 6, 6, 6, 7, 8, 8, 8, 8],
             [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
             [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
             [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
             [8, 8, 8, 8, 8, 8, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
             ]
    t = 0
    for a in arr:
        if t == -1:
            break
        if match('[0-9]', a):
            t = table[t][ord(a)-ord('0')]
        else:
            t = -1
            break
    return t and t != -1


def isAValidV6Section(arr):
    return match('^[0-9a-fA-F]{1,4}$', arr)


class Solution(object):
    def validIPAddress(self, IP):
        v6_data, v4_data = split(':', IP), split('\.', IP)
        if len(v4_data) == 4:
            for data in v4_data:
                if not isAValidV4Section(data):
                    break
            else:
                return 'IPv4'
        if len(v6_data) == 8:
            for data in v6_data:
                if not isAValidV6Section(data):
                    break
            else:
                return 'IPv6'
        return 'Neither'
