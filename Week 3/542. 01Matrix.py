class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # To calculate the paths we need to travers the matrix twice
        # First we traverse from top to bottom calculating only left and up neighbors
        # Then after that we travers from bottom to up calculating only right and bottom neighbors
        
        # We are interested in the lowest neighbor in each traversal 
        # Then we sum 1 representing the current node we are
        
        # Complexity
        # Time O(2*n) we traverse the matrix twice top-bottom / bottom-up
        # Space O(1) we don't have any variable growing together with the input
        
        rowSize = len(mat)
        colSize = len(mat[0])
        
        for i in range(rowSize):
            for j in range(colSize):
                if mat[i][j]:
                    lowest = self.lowestLeftUp(mat, [i,j])                
                    mat[i][j] = lowest + 1
                                        
        for i in reversed(range(rowSize)):
            for j in reversed(range(colSize)):
                if cell := mat[i][j]:
                    lowest = self.lowestRightDown(mat, [i,j])                
                    mat[i][j] = min(cell, lowest+1)
                
                
        return mat
        
        
    def lowestLeftUp(self, matrix, node):
        
        row, col = node       
        left = up = float('inf')
        
        if col > 0:
            #left
            left = matrix[row][col-1]
            
        if row > 0:
            # up
            up = matrix[row-1][col]
        
              
        return min(left, up)
    
    def lowestRightDown(self, matrix, node):
        
        row, col = node       
        right = down = float('inf')
        
        if col+1 < len(matrix[0]):
            right = matrix[row][col+1]
                       
        if row+1 < len(matrix):
            down = matrix[row+1][col]
               
        return min(right, down)