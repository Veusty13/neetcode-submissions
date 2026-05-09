class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {k:[] for k in range(numCourses)}
        for prerequisite in prerequisites:
            first_course = prerequisite[1]
            second_course = prerequisite[0]
            graph[second_course].append(first_course)
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course not in path:
                path.add(course)
                for nei in graph[course]:
                    if not dfs(nei):
                        return False
                path.remove(course)
            return True
        for course in graph:
            if not dfs(course):
                return False
        return True