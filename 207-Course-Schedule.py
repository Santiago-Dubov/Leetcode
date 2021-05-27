# 27/05/21 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = {}
        possible = {}
        
        for i in range(numCourses):
            requirements[i] = []
            possible[i] = []
        
        for ai,bi in prerequisites:
            requirements[ai].append(bi)
            possible[bi].append(ai)

        queue = [i for i in range(numCourses) if len(requirements[i]) == 0]
        visited = []
        if not queue:
            return False

        while queue:
            node = queue.pop()
            if node in visited:
                continue
            visited.append(node)
            children = possible[node]
            for child in children:
                requirements[child].remove(node)
                
                if len(requirements[child]) == 0:
                    queue.append(child)
        
        return len(visited) == numCourses