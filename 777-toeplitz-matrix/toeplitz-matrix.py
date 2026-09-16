class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
    
        for i in range(0,len(matrix)-1):
            for j in range(0,len(matrix[0])-1): 
                if  i+1 < len(matrix) and j+1 <len(matrix[0]) and matrix[i][j] == matrix[i+1][j+1] :
                    continue
                else:
                    return False
        return True
                    


                    

