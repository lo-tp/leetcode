class Solution(object):
    def minSwapsCouplesBetter(self, row):
        res, pos = 0, row[:]
        for index, val in enumerate(row):
            pos[val] = index
        for index in xrange(0, len(row), 2):
            next_val = row[index] ^ 1
            if row[index+1] != next_val:
                res += 1
                tmp_index = pos[next_val]
                row[index+1], row[pos[next_val]
                                  ] = row[pos[next_val]], row[index+1]
                # pos[next_val], pos[row[pos[next_val]]] = index+1, pos[next_val]
                pos[row[pos[next_val]]], pos[next_val] = pos[next_val], index+1
        return res

    def minSwapsCouples(self, row):
        no_swap, res, pos, to_swap, size = set(), 0, {}, set(), len(row)
        for index in xrange(0, size, 2):
            num = row[index]
            pos[num] = index
            if num % 2 and row[index+1] != num-1:
                to_swap.add(index)
            elif not num % 2 and row[index+1] != num+1:
                to_swap.add(index)
        for index in xrange(1, size, 2):
            pos[row[index]] = index

        for index in to_swap:
            if not index in no_swap:
                num = row[index]
                spouse = num-1 if num % 2 else num+1
                spouse_prev_index, spouse_next_index = pos[spouse], index+1
                row[spouse_prev_index], row[spouse_next_index] = row[spouse_next_index], row[spouse_prev_index]
                no_swap.add(index)
                pos[row[spouse_prev_index]] = spouse_prev_index
                pos[row[spouse_next_index]] = spouse_next_index
                res += 1
                index_to_check = spouse_prev_index - \
                    1 if spouse_prev_index % 2 else spouse_prev_index
                num_to_check = row[index_to_check]
                if num_to_check % 2 and row[index_to_check+1] == num_to_check-1:
                    no_swap.add(index_to_check)
                if not num_to_check % 2 and row[index_to_check+1] == num_to_check+1:
                    no_swap.add(index_to_check)
        return res
