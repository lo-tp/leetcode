class Solution(object):
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
