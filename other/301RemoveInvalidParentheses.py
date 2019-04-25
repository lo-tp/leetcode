class Solution(object):
    def removeInvalidParentheses(self, s):
        size, left_to_remove, right_to_remove = len(s), 0, 0
        for i in s:
            if i == '(':
                left_to_remove += 1
            elif i == ')':
                if left_to_remove:
                    left_to_remove -= 1
                else:
                    right_to_remove += 1

        stack = [[0, 0, left_to_remove, right_to_remove, []]]
        data = {}
        while stack:
            index, left_num, left_to_remove, right_to_remove, str = stack.pop()
            if index == size:
                if left_num == 0 and left_to_remove == 0 and right_to_remove == 0:
                    data[''.join(str)] = 1
            elif s[index] == ')':
                index += 1
                if left_num:
                    tmp = str[:]
                    tmp.append(')')
                    stack.append(
                        [index, left_num-1, left_to_remove, right_to_remove, tmp])
                if right_to_remove:
                    tmp = str[:]
                    stack.append(
                        [index, left_num, left_to_remove, right_to_remove-1, tmp])
            elif s[index] == '(':
                index += 1
                tmp = str[:]
                if left_to_remove:
                    stack.append(
                        [index, left_num, left_to_remove-1, right_to_remove, tmp])
                    tmp = str[:]
                tmp.append('(')
                stack.append(
                    [index, left_num+1, left_to_remove, right_to_remove, tmp])
            else:
                tmp = str[:]
                tmp.append(s[index])
                index += 1
                stack.append(
                    [index, left_num, left_to_remove, right_to_remove, tmp])
        return data.keys()


