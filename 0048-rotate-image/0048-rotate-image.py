class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  BRUTE 
        # n = len(matrix)
        # a = [[0]*n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         a[j][n-1-i] = matrix[i][j]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = a[i][j]

        # BETTER 
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        
        

        
