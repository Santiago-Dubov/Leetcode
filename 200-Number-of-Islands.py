class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0 
        
        def dfs(coord):
            #dfs to find all remaining pieces of current island and mark them as '0'
            queue = [coord]
            while queue:
                i,j = queue.pop()
                grid[i][j] = '0'
                for di, dj in [(1,0), (0,1), (-1, 0), (0,-1)]:
                    if (i+di >= 0 and i+di < len(grid)) and (j+dj >= 0 and j+dj < len(grid[0])) and grid[i+di][j+dj] == '1':
                        queue.append((i+di, j+dj))
        
        # search over grid until an island square is found               
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    dfs((i,j))
                    
                    
        return islands