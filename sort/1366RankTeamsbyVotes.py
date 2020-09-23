class Solution(object):
    def rankTeams(self, votes):
        ord_A, scores, res = ord('A'), [[0 for _ in xrange(
            0, 26)] for _ in votes[0]], list(votes[0])
        sz = len(votes[0])
        mapping = {}
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            mapping[i] = ord(i)-ord_A

        for vote in votes:
            for index, letter in enumerate(vote):
                scores[index][mapping[letter]] += 1

        def qc(arr, start, end):
            s, e, m = start, end, arr[start+(end-start)/2]
            while s <= e:
                flag = True
                while flag:
                    for i in xrange(0, sz):
                        if scores[i][mapping[arr[s]]] == scores[i][mapping[m]]:
                            continue
                        elif scores[i][mapping[arr[s]]] < scores[i][mapping[m]]:
                            s += 1
                        else:
                            flag = False
                        break
                    else:
                        if mapping[arr[s]] <= mapping[m]:
                            flag = False
                        else:
                            s += 1
                flag = True
                while flag:
                    for i in xrange(0, sz):
                        if scores[i][mapping[arr[e]]] == scores[i][mapping[m]]:
                            continue
                        elif scores[i][mapping[arr[e]]] > scores[i][mapping[m]]:
                            e -= 1
                        else:
                            flag = False
                        break
                    else:
                        if mapping[arr[e]] >= mapping[m]:
                            flag = False
                        else:
                            e -= 1
                if s <= e:
                    arr[s], arr[e] = arr[e], arr[s]
                    s += 1
                    e -= 1
            if s < end:
                qc(arr, s, end)
            if start < e:
                qc(arr, start, e)
        qc(res, 0, sz-1)
        return ''.join(res[::-1])
    def rankTeams(self, votes):
        ord_A, scores, res = ord('A'), [[0 for _ in xrange(
            0, 26)] for _ in votes[0]], list(votes[0])
        sz = len(votes[0])
        mapping = {}
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            mapping[i] = ord(i)-ord_A

        for vote in votes:
            for index, letter in enumerate(vote):
                scores[index][mapping[letter]] += 1
        def compare(a,b):
            if a==b:
                return 0
            a_index, b_index=mapping[a], mapping[b]
            for score in scores:
                if score[a_index]>score[b_index]:
                    return -1
                elif score[a_index]<score[b_index]:
                    return 1
            return -1 if a_index<b_index else 1

        def qc(arr, start, end):
            s, e, m = start, end, arr[start+(end-start)/2]
            while s <= e:
                while compare(arr[s],m)==-1:
                    s+=1
                while compare(arr[e],m)==1:
                    e-=1
                if s <= e:
                    arr[s], arr[e] = arr[e], arr[s]
                    s += 1
                    e -= 1
            if s < end:
                qc(arr, s, end)
            if start < e:
                qc(arr, start, e)
        qc(res, 0, sz-1)
        return ''.join(res)
