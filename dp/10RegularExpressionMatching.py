class Solution(object):
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
