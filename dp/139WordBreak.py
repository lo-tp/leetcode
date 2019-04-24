class Solution(object):
    def wordBreak(self, s, wordDict):
        dp, word_size, data = {}, len(s), {}
        for i in wordDict:
            if i[0] in data:
                data[i[0]].append(i)
            else:
                data[i[0]] = [i]
        stack = [0]
        while stack:
            start_index = stack.pop()
            if start_index == word_size:
                return True
            elif start_index in dp:
                continue
            else:
                dp[start_index] = 0
                if s[start_index] in data:
                    for partial_match in data[s[start_index]]:
                        offset, partial_length = 0, len(partial_match)
                        while offset < partial_length:
                            word_index = start_index+offset
                            if word_index < word_size and s[word_index] == partial_match[offset]:
                                offset += 1
                            else:
                                break
                        if offset == partial_length:
                            stack.append(start_index+offset)
        return False
