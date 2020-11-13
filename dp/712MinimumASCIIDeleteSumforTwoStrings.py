def help(s):
    return sum([ord(i) for i in s])


class Solution(object):
    def minimumDeleteSum(self, text1, text2):
        sz1, sz2 = len(text1), len(text2)
        dp = ['']*(sz2+1)
        for i in range(0, sz1):
            tmp = ['']
            for j in range(0,  sz2):
                if text1[i] == text2[j]:
                    tmp.append(dp[j]+text2[j])
                elif len(tmp[j]) > len(dp[j+1]):
                    tmp.append(tmp[j])
                elif len(tmp[j]) < len(dp[j+1]):
                    tmp.append(dp[j+1])
                elif help(tmp[j]) > help(dp[j+1]):
                    tmp.append(tmp[j])
                else:
                    tmp.append(dp[j+1])
            dp = tmp
        return sum([ord(i) for i in text1])+sum([ord(i) for i in text2]) - 2*sum([ord(i) for i in dp[-1]])
