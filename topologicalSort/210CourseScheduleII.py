class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        pres, nexts, visited, res = [
            0]*numCourses, [[] for i in xrange(0, numCourses)], {}, []
        for next, prev in prerequisites:
            pres[next] += 1
            nexts[prev].append(next)

        stack = [i for i in xrange(0, numCourses) if not pres[i]]
        while stack:
            node = stack.pop()
            res.append(node)
            visited[node] = True
            for next in [i for i in nexts[node] if i not in visited]:
                prevs[next] -= 1
                if not prevs[next]:
                    stack.append(next)

        return res if len(res) == numCourse else []
