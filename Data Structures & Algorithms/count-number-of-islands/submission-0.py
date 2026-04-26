class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nb_rows = len(grid)
        nb_cols = len(grid[0])
        counter_islands = 0
        path = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= nb_rows or c >= nb_cols or grid[r][c] == "0" or (r,c) in path:
                return 0
            else:
                path.add((r,c))
                res = 1 + dfs(r + 1,c) + dfs(r,c +1) + dfs(r - 1,c) + dfs(r,c - 1)
                if res > 0 :
                    return 1 
                else :
                    return 0
        for r in range(nb_rows):
            for c in range(nb_cols):
                cell = grid[r][c]
                if cell == "1" :
                    counter_islands += dfs(r,c)   
        return counter_islands