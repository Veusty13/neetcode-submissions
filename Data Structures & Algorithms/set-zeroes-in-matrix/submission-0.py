class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        indexes_zero = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    indexes_zero += [[i_,j] for i_ in range(ROWS)]
                    indexes_zero += [[i,j_] for j_ in range(COLS)]
        for indexes in indexes_zero:
            matrix[indexes[0]][indexes[1]] = 0
        
