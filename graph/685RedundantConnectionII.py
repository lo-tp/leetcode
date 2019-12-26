class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        appearance, num = set(), 0
        index = 1
        for input, output in edges:
            if input not in appearance:
                appearance.add(input)
                num += 1
            if output not in appearance:
                appearance.add(output)
                num += 1
            if num == index:
                return [input, output]
            index += 1
