def calculateIndex(index, size):
    return size-index-1


def doNothing(index, _):
    return index


def removeOneType(original, size, remove_num, closing, data):
    res, str, target, opposite, handleIndex, stack = [], original, ')', '(', doNothing, [
        (0, 0, remove_num, x) for x in data]

    if not closing:
        str, target, opposite, handleIndex = original[::-
                                                      1], '(', ')', calculateIndex

    while stack:
        index, opposite_num, remaining_num, removed = stack.pop()
        if not remaining_num:
            res.append(removed)
        if index < size:
            if str[index] == target:
                if opposite_num:
                    stack.append(
                        (index+1, opposite_num-1, remaining_num, removed))
                if remaining_num:
                    new_removed = removed[:]
                    new_removed[handleIndex(index, size)] = ''
                    stack.append(
                        (index+1, opposite_num, remaining_num-1, new_removed))
            elif str[index] == opposite:
                stack.append((index+1, opposite_num+1, remaining_num, removed))
            else:
                stack.append((index+1, opposite_num, remaining_num, removed))

    return [json.loads(d) for d in list(set([json.dumps(k) for k in res]))]


class Solution(object):
    def removeInvalidParenthesesBest(self, s):
        opening_num, closing_num = 0, 0
        for i in s:
            if i == '(':
                opening_num += 1
            elif i == ')':
                if opening_num:
                    opening_num -= 1
                else:
                    closing_num += 1
        size = len(s)
        removed_closing = removeOneType(s, size, closing_num, True, [list(s)])
        # print removed_closing
        removed_opening = removeOneType(
            s, size, opening_num, False, removed_closing)

        return [''.join(k) for k in list(set([''.join(k) for k in removed_opening]))]

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

    def removeOneTypeParenthesses(self, str, to_remove, size, is_opening, ini_stack):
        target, original = '(' if is_opening else ')', str[::-
                                                           1] if is_opening else str
        opposite = '(' if target == ')' else ')'
        res, stack = [], map(lambda x: (0, 0, to_remove, x), ini_stack)
        while stack:
            index, opposite_num, remaining_to_remove, removed = stack.pop()
            if not remaining_to_remove:
                res.append(removed)
            elif original[index] == target:
                if opposite_num:
                    stack.append((index+1, opposite_num-1,
                                  remaining_to_remove, removed.copy()))
                new_removed = removed.copy()
                real_index = size-index-1 if is_opening else index
                new_removed.add(real_index)
                stack.append((index+1, opposite_num,
                              remaining_to_remove-1, new_removed))
            elif original[index] == opposite:
                stack.append((index+1, opposite_num+1,
                              remaining_to_remove, removed.copy()))
            else:
                stack.append((index+1, opposite_num,
                              remaining_to_remove, removed.copy()))
        return res

    def removeInvalidParenthesesBetter(self, s):
        size, opening_to_remove, closing_to_remove = len(s), 0, 0
        for i in s:
            if i == '(':
                opening_to_remove += 1
            elif i == ')':
                if opening_to_remove:
                    opening_to_remove -= 1
                else:
                    closing_to_remove += 1
        array = [i for i in xrange(0, size)]
        result = self.removeOneTypeParenthesses(s, closing_to_remove, size, False,
                                                self.removeOneTypeParenthesses(s, opening_to_remove, size, True, [set()]))
        return list(set(map(lambda data: ''.join(map(lambda x: s[x], filter(lambda index: index not in data, array))), result)))
