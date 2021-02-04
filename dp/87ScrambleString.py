from collections import defaultdict, Counter


class Solution(object):
    def isScramble(self, s1, s2):
        data = defaultdict(set)
        stack = [(s1, False)]
        while stack:
            string, flag = stack.pop()
            if flag:
                sz = len(string)
                for i in range(1, sz):
                    for x in data[string[:i]]:
                        for y in data[string[i:]]:
                            data[string].add(x+y)
                            data[string].add(y+x)
            elif not data[string]:
                sz = len(string)
                if sz == 1:
                    data[string].add(string)
                else:
                    stack.append((string, True))
                    for i in range(1, sz):
                        stack.append((string[:i], False))
                        stack.append((string[i:], False))
        return s2 in data[s1]

class Solution(object):
    def isScramble(self, s1, s2):
        sz1, sz2 = len(s1), len(s2)
        dp = [[[False for _ in range(0, sz1+1)]for _ in range(
            0, sz1)] for _ in range(0, sz1)]
        seen, stack = set(), [(0, 0, sz1, False)]
        while stack:
            i, j, k, flag = stack.pop()
            if flag:
                if k == 1:
                    dp[i][j][k] = s1[i] == s2[j]
                else:
                    for t in range(1, k):
                        if (dp[i][j][t] and dp[i+t][j+t][k-t]) or (dp[i][j+k-t][t] and dp[i+t][j][k-t]):
                            dp[i][j][k] = True
                            break
                seen.add((i, j, k))
            elif (i, j, k) not in seen:
                stack.append((i, j, k, True))
                for t in range(1, k):
                    stack.extend([(i, j, t, False), (i+t, j+t, k-t, False),
                                  (i, j+k-t, t, False), (i+t, j, k-t, False)])
        return dp[0][0][sz1]

    def isScramble(self, s1, s2):
        sz1, sz2 = len(s1), len(s2)
        dp = [[[False for _ in range(0, sz1+1)]for _ in range(
            0, sz1)] for _ in range(0, sz1)]
        seen, stack = set(), [(0, 0, sz1, False)]
        while stack:
            i, j, k, flag = stack.pop()
            if flag:
                if k == 1:
                    dp[i][j][k] = s1[i] == s2[j]
                else:
                    for t in range(1, k):
                        if (dp[i][j][t] and dp[i+t][j+t][k-t]) or (dp[i][j+k-t][t] and dp[i+t][j][k-t]):
                            dp[i][j][k] = True
                            break
                seen.add((i, j, k))
            elif (i, j, k) not in seen:
                stack.append((i, j, k, True))
                if Counter(s1[i:i+k]) == Counter(s2[j:j+k]):
                    for t in range(1, k):
                        stack.extend([(i, j, t, False), (i+t, j+t, k-t, False),
                                      (i, j+k-t, t, False), (i+t, j, k-t, False)])
        return dp[0][0][sz1]
    def isScramble(self, s1, s2):
        sz = len(s1)
        dp, seen, stack = [[[False for _ in range(0, sz+1)]for _ in range(
            0, sz)] for _ in range(0, sz)], set(), [(0, 0, sz, False)]
        while stack:
            start1, start2, sz, flag = stack.pop()
            if flag:
                if sz == 1:
                    dp[start1][start2][1] = s1[start1] == s2[start2]
                else:
                    for t in range(1, sz):
                        if (dp[start1][start2][t] and dp[start1+t][start2+t][sz-t]) or (dp[start1][start2+sz-t][t] and dp[start1+t][start2][sz-t]):
                            dp[start1][start2][sz] = True
                            break
                seen.add((start1, start2, sz))
            elif (start1, start2, sz) not in seen:
                str1, str2 = s1[start1:start1+sz], s2[start2:start2+sz]
                if str1 == str2:
                    dp[start1][start2][sz] = True
                    seen.add((start1, start2, sz))
                if sorted(str1) == sorted(str2):
                    stack.append((start1, start2, sz, True))
                    for t in range(1, sz):
                        stack.extend([(start1, start2, t, False), (start1+t, start2+t, sz-t, False),
                                      (start1, start2+sz-t, t, False), (start1+t, start2, sz-t, False)])
                else:
                    seen.add((start1, start2, sz))
        return dp[0][0][sz]
