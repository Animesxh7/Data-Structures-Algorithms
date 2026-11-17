class Solution:
    def markrow(self,i,matrix,m):
        col = True
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = float('inf')
    def markcol(self,j,matrix,n):
        row = True
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = float('inf')
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # BRUTE
        n = len(matrix)
        m = len(matrix[0])
        row = False
        col = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.markrow(i,matrix,m)
                    self.markcol(j,matrix,n)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0



        