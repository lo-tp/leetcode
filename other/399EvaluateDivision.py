from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        data = defaultdict(lambda: defaultdict(lambda: -1.0))
        for index, _ in enumerate(equations):
            first, second = equations[index]
            # pairs = [(first, second, values[index])]
            if first in data:
                for i in data[first].keys():
                    if i not in data or second not in data[i]:
                        equations.append([i, second])
                        values.append(values[index]/data[first][i])
                        # pairs.append((i, second, values[index]/data[first][i]))
            if second in data:
                for i in data[second].keys():
                    if first not in data or i not in data[first]:
                        equations.append([first, i])
                        values.append(values[index]*data[second][i])
                        # pairs.append((first, i, values[index]*data[second][i]))
            data[first][second] = values[index]
            data[second][first] = 1/values[index]

        return [1.0 if i[0] in data and i[0] == i[1] else data[i[0]][i[1]] for i in queries]

