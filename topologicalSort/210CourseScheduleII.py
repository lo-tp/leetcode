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

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        
        # In graph theory, edges go from u -> v. 
        # Here, u is the prerequisite, and v is the dependent course.
        for v, u in prerequisites:
            in_degree[v] += 1
            adj_list[u].append(v)

        # Nodes with an in-degree of 0 have no incoming edges (no prerequisites)
        stack = [i for i in range(numCourses) if in_degree[i] == 0]
        topological_order = []
        
        while stack:
            node = stack.pop()
            topological_order.append(node)
            
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                
                # If a neighbor's in-degree drops to 0, all its prerequisites are met
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
                    
        # If we couldn't process every node, there was a cycle in the graph
        return topological_order if len(topological_order) == numCourses else []
