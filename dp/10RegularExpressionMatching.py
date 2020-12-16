class Solution(object):
    def isMatchNonRecursiveBetter(self, s, p):
        s_size, p_size = len(s), len(p)
        dp = [[False for i in xrange(0, s_size+1)]
              for k in xrange(0, p_size+1)]
        dp[p_size][s_size] = True
        for p_index in xrange(p_size-1, -1, -1):
            for s_index in xrange(s_size, -1, -1):
                ret = False
                current_match = s_index < s_size and p[p_index] in {
                    '.', s[s_index]}
                if p_index+1 < p_size and p[p_index+1] == '*':
                    ret = (dp[p_index+2][s_index]
                           or (current_match and dp[p_index][s_index+1]))
                else:
                    ret = current_match and dp[p_index+1][s_index+1]
                dp[p_index][s_index] = ret
        return dp[0][0]
    def isMatchNonRecursive(self, str, pattern):
        str_size, pattern_size = len(str), len(pattern)
        dp = [[False for i in xrange(str_size+1)]
              for k in xrange(pattern_size+1)]
        dp[pattern_size][str_size] = True
        for str_index in xrange(str_size, -1, -1):
            for pattern_index in xrange(pattern_size-1, -1, -1):
                if pattern_index == pattern_size:
                    dp[pattern_index][str_index] = str_index == str_size
                else:
                    current_match = str_index < str_size and pattern[pattern_index] in {
                        '.', str[str_index]}
                    if pattern_index+1 < pattern_size and pattern[pattern_index+1] == '*':
                        dp[pattern_index][str_index] = dp[pattern_index +
                                                          2][str_index] or (current_match and dp[pattern_index][str_index+1])
                    else:
                        dp[pattern_index][str_index] = current_match and dp[pattern_index+1][str_index+1]
        return dp[0][0]
    def dp(self, str_index, pattern_index):
        if (str_index, pattern_index) not in self.data:
            if pattern_index == self.pattern_size:
                self.data[(str_index, pattern_index)
                          ] = str_index == self.str_size
            else:
                current_match = str_index < self.str_size and self.pattern[pattern_index] in {
                    self.str[str_index], '.'}
                if pattern_index+1 < self.pattern_size and self.pattern[pattern_index+1] == '*':
                    self.data[(str_index, pattern_index)] = self.dp(
                        str_index, pattern_index+2) or current_match and self.dp(str_index+1, pattern_index)
                else:
                    self.data[(str_index, pattern_index)] = current_match and self.dp(
                        str_index+1, pattern_index+1)
        return self.data[(str_index, pattern_index)]



    def isMatch(self, s, p):
        self.data, self.str, self.pattern, self.str_size, self.pattern_size = {
        }, s, p, len(s), len(p)
        return self.dp(0, 0)
     
    def isMatch(self, s, p):
        s_sz, p_sz = len(s), len(p)
        dp = [False for _ in range(0, p_sz+1)]
        dp[0] = True
        for i in range(1, p_sz, 2):
            if p[i] == '*':
                dp[i+1] = True
            else:
                break
        for i in range(0, s_sz):
            tmp = [False]*(p_sz+1)
            for j in range(0, p_sz):
                if p[j] == '*':
                    tmp[j+1] = tmp[j] or ((p[j-1] ==
                                           '.' or p[j-1] == s[i]) and dp[j+1])
                elif p[j] == '.':
                    tmp[j+1] = dp[j]
                else:
                    tmp[j+1] = s[i] == p[j] and dp[j]
            dp = tmp
        return dp[-1]
