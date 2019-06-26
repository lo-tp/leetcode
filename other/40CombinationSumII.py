def qc(arr, start, end):
    s, e, m = start, end, arr[start+(end-start)/2]
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    if s < end:
        qc(arr, s, end)
    if start < e:
        qc(arr, start, e)


class Solution(object):
    def combinationSum2(self, candidates, target):
        visited, res = {}, []
        if candidates:
            qc(candidates, 0, len(candidates)-1)
            stack = []
            for index, num in enumerate(candidates):
                key = str(num)
                if key not in visited:
                    visited[key] = True
                    stack.append((num, index+1, [num]))
            while stack:
                sum, last_index, path = stack.pop()
                if sum == target:
                    res.append(path)
                elif sum < target:
                    for index, num in enumerate(candidates[last_index:]):
                        new_path = path[:]
                        new_path.append(num)
                        key = ' '.join([str(ele) for ele in new_path])
                        if key not in visited:
                            visited[key] = True
                            stack.append(
                                (sum+num, last_index+index+1, new_path))
        return res

