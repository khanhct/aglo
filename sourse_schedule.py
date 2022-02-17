class Solution:
    def canFinish(self, numCourses, prerequisites):
        prerequisites.sort(key=lambda a: a[0])

        visited = [0] * numCourses
        sorted_courses = []
        for i in range(numCourses):
            if visited[i] == 2:
                continue
            visited[i] = 1
            sorted_courses.append(i)
            val = self.dfs(i, prerequisites, visited, sorted_courses)
            if val:
                return []
            visited[i] = 2

        return list(sorted_courses)

    def dfs(self, node, prerequisites, visited, sorted_courses):
        stack = []

        for prerequisite in prerequisites:
            if prerequisite[0] == node:
                if visited[prerequisite[1]] == 1:
                    return True
                if visited[prerequisite[1]] == 0:
                    stack.insert(0, prerequisite[1])
        if not stack:
            if node in sorted_courses:
                sorted_courses.remove(node)
            sorted_courses.insert(0, node)
        else:
            sorted_courses.append(node)

        while stack:
            n = stack.pop(0)
            visited[n] = 1
            if self.dfs(n, prerequisites, visited, sorted_courses):
                return True
            visited[n] = 2



sol = Solution()
# print(sol.canFinish(2, [[0, 1]]))
# print(sol.canFinish(2, [[1, 0], [0, 1]]))
print(sol.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))

