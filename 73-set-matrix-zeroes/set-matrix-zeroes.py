class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = 0
        column = 0
        mat = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                   row = i
                   column = j
                   mat.append([row,column])
                else:
                    pass
        for row,col in mat:
            for j in range(len(matrix[0])):
                matrix[row][j] =0
            for i in range(len(matrix)):
                matrix[i][col] =0
        return matrix