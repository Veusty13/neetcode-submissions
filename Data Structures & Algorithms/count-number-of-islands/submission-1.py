class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def flood_island_from_coordinates(i,j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            flood_island_from_coordinates(i, j+1)
            flood_island_from_coordinates(i+1, j)
            flood_island_from_coordinates(i, j-1)
            flood_island_from_coordinates(i-1, j)
        ROWS = len(grid)
        COLS = len(grid[0])
        nb_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    flood_island_from_coordinates(i, j)
                    nb_islands += 1
        return nb_islands
