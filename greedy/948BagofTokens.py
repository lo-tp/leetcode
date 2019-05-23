def qc(arr, start, end):
    s, e, m = start, end, arr[start+(end-start)/2]
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    if s < end:
        qc(arr, s, end)
    if start < e:
        qc(arr, start, e)


class Solution(object):
    def bagOfTokensScore(self, tokens, points):
        cur, start, end, res = 0, 0, len(tokens)-1, 0
        if end >= start:
            qc(tokens, start, end)
            while start <= end:
                if points >= tokens[start]:
                    points -= tokens[start]
                    cur += 1
                    res = max(cur, res)
                    start += 1
                elif cur:
                    points += tokens[end]
                    cur -= 1
                    end -= 1
                else:
                    break
        return res

